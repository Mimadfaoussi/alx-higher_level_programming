#include "lists.h"

/**
 * check_cycle-checks if a singly linked list has a cycle in it.
 * @list:the linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t	*t1;
	listint_t	*t2;

	if (list == NULL || list->next == NULL)
		return (0);
	t1 = list;
	t2 = list->next;
	while (t2 != NULL && t1 != t2)
	{
		t2 = t2->next;
		t1 = t1->next;
		if (t2 != t1 && t2 != NULL)
			t2 = t2->next;
	}
	if (t1 == t2)
		return (1);
	return (0);
}
