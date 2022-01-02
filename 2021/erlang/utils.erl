-module(utils).
-export([read_lines/1, to_list_of_ints/1]).

-spec read_lines(string()) -> list(string()).
read_lines(FileName) ->
  {ok, Bin} = file:read_file(FileName),
  Lines = string:tokens(binary_to_list(Bin), "\n"),
  Lines.

-spec to_list_of_ints(list(string())) -> list(integer()).
to_list_of_ints(L) -> [to_int(X) || X <- L].

-spec to_int(string()) -> integer().
to_int(Str) ->
  {N, _} = string:to_integer(Str),
  N.
