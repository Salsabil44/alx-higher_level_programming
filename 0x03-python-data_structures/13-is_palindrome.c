#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *x = NULL, *x2 = NULL;

	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_nodeint(&x, head2->n);
		head2 = head2->next;
	}
	x2 = x;
	while (*head != NULL)
	{
		if ((*head)->n != x2->n)
		{
			free_listint(x);
			return (0);
		}
		*head = (*head)->next;
		x2 = x2->next;
	}
	free_listint(x);
	return (1);
}
