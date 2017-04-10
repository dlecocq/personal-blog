---
layout: post
status: publish
published: true
title: MPI_Datatype
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 898
date: '2010-08-22 11:47:11 -0700'
date_gmt: '2010-08-22 18:47:11 -0700'
categories:
- computer science
tags:
- mpi
- datatypes
comments:
- id: 2212
  author: tinku
  author_email: tinkuminku123@gmail.com
  date: '2012-05-30 10:08:04 -0700'
  date_gmt: '2012-05-30 17:08:04 -0700'
  content: "Thanks for the article!\r\n\r\nOne correction: \r\nint barDatatype; should
    be MPI_Datatype barDatatype;"
- id: 2246
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2012-06-13 16:00:46 -0700'
  date_gmt: '2012-06-13 23:00:46 -0700'
  content: Very true! Should be correct now -- thanks!
- id: 3161
  author: Reza
  author_email: mrektefa@gmail.com
  date: '2014-08-07 21:02:02 -0700'
  date_gmt: '2014-08-08 04:02:02 -0700'
  content: "typo issue in MPI_Dataype types[3] = {MPI_INT, MPI_CHAR, MPI_DOUBLE};\r\nMPI_Dataype
    should be MPI_Datatype"
---
It has been a while since I've had to work with MPI, but recently I had to learn a new trick with it.  MPI provides ways to convey data between processes in a number of ways, from broadcasts to scatters to all-gathers.  But obviously you have to provide a certain amount of information about the structure of the data, not the least of which is the datatype.

MPI defines enumerated constants for the basic data types in C: `MPI_CHAR`, `MPI_INT`, etc., and for the most part these will suffice.  But what if you want to scatter your own struct?  This can be done through a number of utility functions, but the most versatile seems to be `MPI_Type_struct()`.

You let MPI know how many different blocks, or chunks of memory there are, their lengths, their offsets and types, and then what variable to store the resulting integer handle in.  So if we had a struct:

```c++
typedef struct {
    int var;
    char string[STRING_LENGTH];
    double foo;
} bar;
```

We would first indicate that there are three blocks, of lengths 1, STRING_LENGTH and 1:

```c++
int count = 3;
int lengths[3] = {1, STRING_LENGTH, 1};
```

The offsets indicate the byte offsets from the base address of each of the types in the structure.  For this example, the "var" variable is the first, and thus has offset 0.  On the other hand, "string" will have an offset that is `sizeof(int)`, and "foo" will appear after the int and the string of length STRING_LENGTH:

```c++
MPI_Aint offsets[3] = {0, sizeof(int), sizeof(int) + STRING_LENGTH};
MPI_Dataype types[3] = {MPI_INT, MPI_CHAR, MPI_DOUBLE};
```

To finish up, we ask MPI to fill an integer we declare with the handle that will hereafter refer to this struct for the purposes of MPI.  Then, we commit it, and it's ready for use!

```c++
/* Corrected by commenter `tinku`: int -> MPI_Datatype */
MPI_Datatype barDatatype;
MPI_Type_struct(count, lengths, offsets, types, &barDatatype);
MPI_Type_commit(&barDatatype);
```

Now if you have an array of bar structs, you can use `scatterv` with it and your new datatype, or `bcast` for that matter.  It's business as usual, as if it were any of the include base datatypes in MPI.
