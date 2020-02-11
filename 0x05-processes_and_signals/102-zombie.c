#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - puts the calling process in a infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			/* child process */
			exit(0);
		}
		else if (pid > 0)
		{
			/* parent process */
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
		{
			printf("fork() failed!\n");
			return (1);
		}
	}
	infinite_while();

	return (0);
}
