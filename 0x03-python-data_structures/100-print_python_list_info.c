#include <Python.h>

void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - prints some basic info about Python lists 
 * @p: pyobject list.
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, n;
	PyObject *ob;

	size = Py_SIZE(p);
	alloc = ((PylistObject *)p)->allocated;

	printf("[*] Size of the Python list = %d/n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (n = 0; n < size; n++)
	{
		printf("Element %d: ", n);

		ob = PyList_GelItem(p, n);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
