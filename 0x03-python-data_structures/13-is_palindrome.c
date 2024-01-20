#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head list
 *
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palind(head, *head));
}

/**
 * palind - function to find if palind
 * @head: head of the list
 * @end: end of the list
 *
 * Return: 0 or 1
*/
int palind(listint_t **head, listtint_t *end)
{
	if (end == NULL)
		return (1);
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
