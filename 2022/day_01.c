#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main(int argc, char **argv)
{
	FILE *fp;
	char *line = NULL;
	size_t linecap = 0;
	ssize_t linelen;
	unsigned int max_calories;
	unsigned int curr_total;

	if (argc != 2) {
		fprintf(stderr, "Usage: %s: <input_file_name>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if ((fp = fopen(argv[1], "r")) == NULL) {
		fprintf(stderr, "Could not open file\n");
		exit(EXIT_FAILURE);
	}

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

	printf("Answer: %d\n", max_calories);

	free(line);
	fclose(fp);
	exit(EXIT_SUCCESS);
}
