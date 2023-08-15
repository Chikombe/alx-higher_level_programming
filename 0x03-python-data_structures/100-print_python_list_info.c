#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, itr;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (itr = 0; itr < size; itr++)
	{
		printf("Element %d: ", itr);

		obj = PyList_GetItem(p, itr);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
