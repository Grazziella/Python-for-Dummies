#!/usr/bin/env python
# -*- coding: utf-8 -*-

# shebang
# encoding
# make a function that inform a person's sign depending on their day of birth!
# Aquarius 21 Jan - Feb 21 ... Pisces 22 Feb - 21 Mar ... Aries 22 March - 20 Apr ...
# Taurus 21 apr - May 21 ...  Gemini May 22 - June 21 ... Cancer June 22 - Jul 22...
# Leo 23 Jul - 22 Aug...   Virgo 23 Aug - 22 Sep...  Libra Sep 23 - Oct 23
# Scorpio  Oct 24 - Nov 21 ... Sagittarius Nov 22 - Dez 21 ... Capricorn Dec 22 - 20 Jan
# como  input para dia, input para mês
# dependendo do mês se for maior ou menor 21/22 -> signo
# considerar que o mês pode ser input como abreviatura: criar uma função para transformar mês abb em number - cheated!!!!
#MELHORAMENTO: tentar fazer que o input tbm possa ser feito com a primeira letra minúscula!

def month_abb_to_num(month):
	return{
	 'Jan': 1,
	 'Feb': 2,
	 'Mar': 3,
	 'Apr': 4,
	 'May': 5,
	 'Jun': 6,
	 'Jul': 7,
	 'Aug': 8,
	 'Sep': 9,
	 'Oct': 10,
	 'Nov': 11,
	 'Dec': 12} [month]

def horoscope(day, month):
    day = int(input('What day were you born? '))
    month = int(input('What month were you born? '))
	if month == 1:
		if day >= 21:
			sign = 'Aquarius'
		else:
			sign = 'Capricorn'
	if month == 2:
		if day >= 22:
			sign = 'Pisces'
		else:
			sign = 'Aquarius'
	if month == 3:
		if day >= 22:
			sign = 'Aries'
		else:
			sign = 'Pisces'
	if month == 4:
		if day >= 21:
			sign = 'Taurus'
		else:
			sign = 'Aries'
	if month == 5:
		if day >= 22:
			sign = 'Gemini'
		else:
			sign = 'Taurus'
	if month == 6:
		if day >= 22:
			sign = 'Cancer'
		else:
			sign = 'Gemini'
	if month == 7:
		if day >= 23:
			sign = 'Leo'
		else:
			sign = 'Cancer'
	if month == 8:
		if day >= 23:
			sign = 'Virgo'
		else:
			sign = 'Leo'
	if month == 9:
		if day >= 23:
			sign = 'Libra'
		else:
			sign = 'Virgo'
	if month == 10:
		if day >= 24:
			sign = 'Scorpio'
		else:
			sign = 'Libra'
	if month == 11:
		if day >= 22:
			sign = 'Sagittarius'
		else:
			sign = 'Scorpio'
	if month == 12:
		if day >= 22:
			sign = 'Capricorn'
		else:
			sign = 'Sagittarius'
	return sign
print(horoscope(day, month))
