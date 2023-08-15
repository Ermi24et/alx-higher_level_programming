#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - a function that checks if it is palindrome
 * @head: a pointer input
 * Return: 0 if it isn't palindrome, oyherwise 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *f_half = *head, *s_half = *head;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (s_half != NULL && f_half != NULL &&
			f_half->next != NULL)
	{
		s_half = s_half->next;
		f_half = f_half->next->next;
	}
	s_half = reverse_list(&s_half);
	f_half = *head;
	while (f_half != NULL && s_half != NULL)
	{
		if (f_half->n != s_half->n)
			return (0);
		f_half = f_half->next;
		s_half = s_half->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a list
 * @head: a pointer input
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *next = *head, *current = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = current;
		current = *head;
		*head = next;
	}
	*head = current;
	return (*head);
}
