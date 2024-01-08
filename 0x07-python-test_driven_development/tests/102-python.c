#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_string(PyObject *p)
{
    PyObject *repr = PyObject_Repr(p);  // Use repr to get the string representation
    PyObject *str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

    printf("[.] string object info\n");

    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
    printf("  value: %s\n", PyBytes_AsString(str));
    printf("  repr: %s\n", PyBytes_AsString(repr));  // Print the representation
}

