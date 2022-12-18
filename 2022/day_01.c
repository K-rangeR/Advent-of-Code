#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROOT 0
#define LEFT_CHILD 1
#define RIGHT_CHILD 2

void
update_calories_heap(unsigned int min_heap[], unsigned int total)
{
	int swap_idx;
	unsigned int tmp;

	if (total < min_heap[ROOT])
		return;

	swap_idx = ROOT;
	min_heap[ROOT] = total;
	if (min_heap[LEFT_CHILD] < min_heap[RIGHT_CHILD])
		swap_idx = LEFT_CHILD;
	else
		swap_idx = RIGHT_CHILD;

	if (min_heap[ROOT] > min_heap[swap_idx]) {
		tmp = min_heap[ROOT];
		min_heap[ROOT] = min_heap[swap_idx];
		min_heap[swap_idx] = tmp;
	}
}

unsigned int
part_1(FILE *fp)
{
	char *line = NULL;
	size_t linecap = 0;
	ssize_t linelen;
	unsigned int max_calories;
	unsigned int curr_total;

	max_calories = 0;
	curr_total = 0;
	while ((linelen = getline(&line, &linecap, fp)) > 0) {
		if (strcmp(line, "\n") == 0) {
			max_calories = (curr_total > max_calories) ? curr_total : max_calories;
			curr_total = 0;
		} else {
			curr_total += (unsigned int)atoi(line);
		}
	}

	free(line);
	return max_calories;
}

unsigned int
part_2(FILE *fp)
{
	char *line = NULL;
	size_t linecap = 0;
	ssize_t linelen;
	unsigned int answer;
	unsigned int curr_total;
	unsigned int top_three_calories[3] = { 0, 0, 0 };

	curr_total = 0;
	while ((linelen = getline(&line, &linecap, fp)) > 0) {
		if (strcmp(line, "\n") == 0) {
			update_calories_heap(top_three_calories, curr_total);	
			curr_total = 0;
		} else {
			curr_total += (unsigned int)atoi(line);
		}
	}

	answer = 0;
	for (int i = 0; i < 3; ++i)
		answer += top_three_calories[i];

	free(line);
	return answer;
}


int
main(int argc, char **argv)
{
	FILE *fp;

	if (argc != 2) {
		fprintf(stderr, "Usage: %s: <input_file_name>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if ((fp = fopen(argv[1], "r")) == NULL) {
		fprintf(stderr, "Could not open file\n");
		exit(EXIT_FAILURE);
	}

	printf("Part #1 answer: %d\n", part_1(fp));
	rewind(fp);
	printf("Part #2 answer: %d\n", part_2(fp));

	fclose(fp);
	exit(EXIT_SUCCESS);
}
