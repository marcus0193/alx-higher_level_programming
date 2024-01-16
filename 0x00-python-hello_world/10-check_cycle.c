#include <stdio.h>
#include <stdlib.h>
#include "list.h"

/**
 * check_cycle - list cyclical check
 * @list: list check pointer
 *
 * Return: 1 is cycle 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
