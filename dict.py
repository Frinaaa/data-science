{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "213efcf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dict1 : {1: 'water', 2: 'Shafnas'}\n",
      "Dict2 : {3: 'water', 4: 'fire'}\n",
      "Merged dict : {1: 'water', 2: 'Shafnas', 3: 'water', 4: 'fire'}\n"
     ]
    }
   ],
   "source": [
    "d1 = {1: 'water', 2: 'Shafnas'}\n",
    "d2 = {3: 'water', 4 : 'fire'}\n",
    "\n",
    "print(\"Dict1 :\",d1)\n",
    "print(\"Dict2 :\",d2)\n",
    "\n",
    "merge_dict=d1.copy()\n",
    "merge_dict.update(d2)\n",
    "\n",
    "print(\"Merged dict :\",merge_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bc842e60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter numbers for the first list: 3,5\n",
      "Enter numbers for the second list: 5,7\n",
      "Common number found: True\n"
     ]
    }
   ],
   "source": [
    "list1 = list(map(int, input(\"Enter numbers for the first list: \").split(',')))\n",
    "\n",
    "list2 = list(map(int, input(\"Enter numbers for the second list: \").split(',')))\n",
    "\n",
    "common_found = False\n",
    "for num in list1:\n",
    "    if num in list2:\n",
    "        common_found = True\n",
    "        break\n",
    "\n",
    "print(\"Common number found:\", common_found)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86f45bbd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d748cf3d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
