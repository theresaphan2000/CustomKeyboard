#include <stdio.h> 
#include <Python.h> 



//Define a new exception object for our module 
static PyObject *exmodError; 

//make a c function that recieves in python message 
static PyObject* exmod_get_key(PyObject* self, PyObject *args){
	const char* msg; 
	int sts=0; 

	// PyArg_ParseTuble takes in PyObject argument, a (const char*), and the address to the message, must meet these parameters
	if(!PyArg_ParseTuble(args, "s", &msg)){
		return NULL; // return NULL ERROR CODE if none 
	} 


	return NULL; 
}
