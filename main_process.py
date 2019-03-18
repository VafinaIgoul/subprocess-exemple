# coding: utf-8
import subprocess


def subprocess_example():
    input_file = open('subprocess.txt')
    process_for_add = subprocess.Popen(
        ["python.exe",  "add.py"],
        stdin=input_file,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    input_file.close()
    process_for_exponentiation = subprocess.Popen(
        ["python.exe",  "exponentiation.py"],
        stdin=process_for_add.stdout,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)

    process_for_division = subprocess.Popen(
        ["python.exe", "division.py"],
        stdin=process_for_exponentiation.stdout,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)

    out, err = process_for_division.communicate()
    print out
    print err


subprocess_example()
