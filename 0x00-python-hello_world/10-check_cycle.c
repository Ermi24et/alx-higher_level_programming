#include "lists.h"

/**
 *check_cycle - checks a lnked list if it is circular
 *@list: head
 *Return: 1 if it is circular, 0 if it isn't
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *check = list;

	while (current && check && check->next)
	{
		current = current->next;
		check = check->next->next;
		if (current == check)
		{
			return (1);
		}

	}
	return (0);
}
