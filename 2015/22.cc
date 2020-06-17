#include <iostream>
#include <limits>
#include <vector>
#include <deque>
#include <algorithm>
#include <memory>


int min_mana_spent = std::numeric_limits<int>::max();



class GoodGuy {
  int hp;
  int mana;
  int armor; 
public:
  GoodGuy(int hit_points, int m, int a) : hp{hit_points}, mana{m}, armor{a} {}
  void take_damage(int by) { hp = std::max(hp-by, 1); }
  void heal(int by) { hp += by; }
  bool is_dead() { return hp <= 0; }
  void update_armor(int new_armor) { armor = new_armor; }
  void use_mana(int used) { mana -= used; }
  void restore_mana(int amount) { mana += amount; }
  bool out_of_mana() { return mana == 0; }
  int get_mana() const { return mana; }
};


class Enemy {
  int hp;
  int damage;
public:
  Enemy(int hit_points, int d) : hp{hit_points}, damage{d} {}
  void take_damage(int by) { hp -= by; }
  bool is_dead() { return hp <= 0; }
  int attack() { return damage; }
};


class Spell {
protected:
  const int mana_cost;
  const std::string name;
public:
  Spell(int mc, const std::string n) : mana_cost{mc}, name{n} {}
  
  virtual ~Spell() = default;

  // Does something to the enemy and player, returns true if the spell
  // is complete, or false otherwise (for effects)
  virtual bool perform(GoodGuy&, Enemy&) = 0;

  // Virtual copy constructor
  virtual Spell *clone() = 0;

  bool operator==(const Spell& spell) {
    return name == spell.name;
  }

  int get_mana_cost() const { return mana_cost; }
  std::string get_name() const { return name; }
};


class Magic_Missile : public Spell {
  const int damage = 4;
public:
  Magic_Missile(const std::string name, int mana_cost, int d) 
    : Spell(mana_cost, name), damage {d} {}

  Magic_Missile(const Magic_Missile& rhs) 
    : Spell(rhs.mana_cost, rhs.name), damage {rhs.damage} {}

  ~Magic_Missile() = default;

  virtual bool perform(GoodGuy& player, Enemy& enemy) {
    enemy.take_damage(damage);
    return true;
  }

  Spell *clone() {
    return new Magic_Missile(*this);
  }
};


class Drain : public Spell {
  const int damage = 2;
  const int heals_for = 2;
public:
  Drain(const std::string name, int mc, int d, int h) 
    : Spell(mc, name), damage{d}, heals_for{h} {}

  Drain(const Drain& rhs)
    : Spell(rhs.mana_cost, rhs.name), damage{rhs.damage}, heals_for{rhs.heals_for} {}

  ~Drain() = default;

  virtual bool perform(GoodGuy& player, Enemy& enemy) {
    enemy.take_damage(damage);
    player.heal(heals_for);
    return true;
  }

  Spell *clone() {
    return new Drain(*this);
  }
};


class Shield : public Spell {
  int effect_len = 6;
  const int armor_inc = 7;
public:
  Shield(const std::string name, int mc, int len, int ai)
    : Spell(mc, name), effect_len{len}, armor_inc{ai} {}

  Shield(const Shield& rhs)
    : Spell(rhs.mana_cost, rhs.name), effect_len{rhs.effect_len}, armor_inc{rhs.armor_inc}
  {}

  ~Shield() = default;

  virtual bool perform(GoodGuy& player, Enemy& enemy) {
    player.update_armor(armor_inc);
    effect_len -= 1;
    if (effect_len == 0) {
      player.update_armor(0);
      return true;
    }
    return false;
  }

  Spell *clone() {
    return new Shield(*this);
  }
};


class Poison : public Spell {
  int effect_len = 6;
  const int damage = 3;
public:
  Poison(const std::string name, int mc, int len, int d) 
    : Spell(mc, name), effect_len{len}, damage{d} {}

  Poison(const Poison& rhs)
    : Spell(rhs.mana_cost, rhs.name), effect_len{rhs.effect_len}, damage{rhs.damage} {}

  ~Poison() = default;

  virtual bool perform(GoodGuy& player, Enemy& enemy) {
    enemy.take_damage(damage);
    effect_len -= 1;
    if (effect_len == 0) {
      return true;
    }
    return false;
  }

  Spell *clone() {
    return new Poison(*this);
  }
};


class Recharge : public Spell {
  int effect_len = 5;
  const int recharge_amt = 101;
public:
  Recharge(const std::string name, int mc, int len, int r) 
    : Spell(mc, name), effect_len{len}, recharge_amt{r} {}

  Recharge(const Recharge& rhs)
    : Spell(rhs.mana_cost, rhs.name), effect_len{rhs.effect_len}, recharge_amt{rhs.recharge_amt} {}

  ~Recharge() = default;

  virtual bool perform(GoodGuy& player, Enemy& enemy) {
    player.restore_mana(recharge_amt);
    effect_len -= 1;
    if (effect_len == 0) {
      return true;
    }
    return false;
  }

  Spell *clone() {
    return new Recharge(*this);
  }
};


using Active_Spells_List = std::deque<std::shared_ptr<Spell>>;


bool can_cast(const GoodGuy& player, 
              Spell *spell, 
              const Active_Spells_List active_spells)
{
  if (player.get_mana() < spell->get_mana_cost()) {
    return false;
  }

  for (auto curr : active_spells) {
    if (*curr == *spell) {
      return false;
    }
  }

  return true;
}


void fight(GoodGuy player, Enemy enemy, 
           int turn_order, int mana_spent,
           Active_Spells_List active_spells,
           const std::vector<Spell*>& spells)
{
  for (auto spell = active_spells.begin(); spell < active_spells.end(); spell++) {
    if ((*spell)->perform(player, enemy)) {
      active_spells.erase(spell);
    }
    if (enemy.is_dead()) {
      min_mana_spent = std::min(mana_spent, min_mana_spent); 
      return;
    }
  }

  if (turn_order % 2 == 0) {
    player.take_damage(enemy.attack());
    fight(player, enemy, turn_order+1, mana_spent, active_spells, spells);
  } else {
    if (player.out_of_mana() || player.is_dead()) {
      return;
    }

    for (auto spell : spells) {
      if (can_cast(player, spell, active_spells)) {
        std::shared_ptr<Spell> new_spell_ptr {spell->clone()};
        active_spells.push_front(new_spell_ptr);
        player.use_mana(spell->get_mana_cost());
        fight(player, enemy, turn_order+1, mana_spent+spell->get_mana_cost(), 
              active_spells, spells); 
        player.restore_mana(spell->get_mana_cost());
      }
    }
  }
}


int main()
{
  GoodGuy player {50, 500, 0};
  Enemy enemy {51, 9};

  Magic_Missile mm{"magic missile", 53, 4};
  Drain d{"drain", 73, 2, 2};
  Shield s{"shield", 113, 6, 7};
  Poison p{"poison", 173, 6, 3};
  Recharge r{"recharge", 229, 5, 101};

  std::vector<Spell*> spells { &mm, &d, &s, &p, &r };
  Active_Spells_List active_spells {};
  fight(player, enemy, 1, 0, active_spells, spells); 

  std::cout << "Answer: " << min_mana_spent << "\n";
  return 0;
}
