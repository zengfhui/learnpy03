#!/usr/bin/env python3

import sys

'''
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]
index = args.index('-o')
outputfile= args[index+1]
'''


class Args():
	def __init__(self):
		self.args = sys.argv[1:]

	def _value_after_option(self,option):
		try:
			index = self.args.index(option) + 1
			return self.args[index]
		except:
			print("Parameter Error")

	@property
	def _path_configfile(self):
		return self._value_after_option('-c')

	@property
	def _path_userdatafile(self):
		return self._value_after_option('-d')

	@property
	def _path_outputfile(self):
		return self._value_after_option('-o')

args = Args()

class Config():
	def __init__(self):
		self.config = self._read_configfile()

	def _read_configfile(self):

		configfile = args._path_configfile
		self.config =dict()
		with open(configfile) as file:
			for line in file.readlines():
				key,value = line.strip.split('=')
				try:
					self.config[key] = float[value]
				except:
					print('configfile have error')
					exit()

	def _get_config(self,key):
		try:
			return self.config[key]
		except:
			print(key,'on exist')
			exit()

	def _JishuL(self):
		return(_get_config('JiShuL'))

	def _JishuH(self):
		return(_get_config('JiShuH'))	

	def _rate(self):
		return sum([
			_get_config('YangLao'),
			_get_config('YiLiao'),
			_get_config('ShiYe'),
			_get_config('GongShang'),
			_get_config('ShengYu'),
			_get_config('GongJiJin'),
			])


config = Config()




class UserData():
	def __init__(self):
		self.userdate = self._read_userdatafile()

	def _read_userdatafile(self):
		self.userdata  = []
		userdatafile = args._path_userdatafile
		userdata = []
		with open(userdatafile) as file:
			for line in f.readlines():
				name,salary_string = line.strip().split(',')
				try:
					salary = int(salary_string)
				except:
					print("userdatafile have error")
					exit()
			userdata.append([name,salary])
		return userdata

	def __iter__(seld):
		return iter(self.userdata)

class TaxCalc():
	def __init__(self,userdata):
		self.userdata = userdata

	@property
	def calc_insurance_money(self,salary):
		rate = config._rate
		insurance_money = 0
		if salary < config._JiShuL:
			insurance_money = 2193.0 * rate
		elif salary > config._JiShuH:
			insurance_money = 16646.0* rate
		else:
			insurance_money = salary * rate	
		return insurance_money

	def calc_tax_and_remain(self,salary):
		amount = salary * (1 - config._rate) - 3500
		tax = 0
		if amount < 0:
		 	tax = 0
		elif amount < 1500:
		 	tax = amount * 0.03
		elif tax < 4500:
		 	tax = (amount * 0.1) - 105
		elif amount < 9000:
		 	tax = (amount * 0.2) - 555
		elif amount < 35000:
		 	tax = (amount * 0.25) - 1005
		elif amount < 55000:
		 	tax =  (amount * 0.3) - 2755
		elif amount < 80000:
		 	tax = (amount * 0.35) - 5505
		else:
		 	tax = (amount * 0.450) -13505

		remain  = salary - calc_insurance_money(salary) - tax
	
		return '{:f}'.format(tax),'{:f}'.format(remain)


	def calc_for_all_userdata(self):
		result = []
		for name,salary in self.userdata:
			data = [name,salary]
			insurance_money = calc_insurance_money(salary)
			tax,remain = calc_tax_and_remain(salary)
			data += [insurance_money,tax,remain]
			result.append(data)
		return result

	def export(self):
		result = calc_for_all_userdata()
		with open(args._path_outputfile,'w',newline = '') as file:
			writer = csv.writen(file)
			writer.writerows(result)

if __name__ == 'main':
	d = UserData()
	d.export


'''

	def __init__(self,userdatafile):
		self._userdata = dict()
		with open(userdatafile) as file:
			count = 0
			for line in file:
				count += 1
				tline = line.strip('\n')
				tmp = tline.split(':')
				self._userdata[count] = [tmp[0],int(tmp[1])]
		self.number = count


#				tmp = ['100','1000']
#				d = dict()
#				d[1] = [tmp[0],int(tmp[1])]
#
#				print(d)
#				d = 1 : ['100',1000]
#
#				print(d[1][0])
#				'100'

	def caculator(self,salary,Config):

		rate = Config.get_rate()	 
		shebao = 0.0
		if salary < Config.get_JiShuL:
			shebao = 2193.0 * rate
		elif salary > Config.get_JiShuH:
			shebao = 16646.0* rate
		else:
			shebao = salary * rate
		
		amount = salary * (1 - rate) - 3500
		tax = 0
		if amount < 0:
		 	tax = 0
		elif amount < 1500:
		 	tax = amount * 0.03
		elif tax < 4500:
		 	tax = (amount * 0.1) - 105
		elif amount < 9000:
		 	tax = (amount * 0.2) - 555
		elif amount < 35000:
		 	tax = (amount * 0.25) - 1005
		elif amount < 55000:
		 	tax =  (amount * 0.3) - 2755
		elif amount < 80000:
		 	tax = (amount * 0.35) - 5505
		else:
		 	tax = (amount * 0.450) -13505

		after_salary = salary - shebao - tax
		s = []
		s.append(shebao)
		s.append(tax)
		s.append(after_salary)
		return s
		
	def dumpptofile(self,outputfile,Config):
		sf = []
		stand ='0123456789.'
		for k in range(self.number):
			s = json.dumps(self._userdata[k+1])
			tmp = s.split(',')
			for i in range(len(tmp)):	
				for c in tmp[i]:
					if not c in stand:
						tmp[i] = tmp[i].replace(c,'')

			dit = ','
			sf.append (dit.join(tmp))
		print(sf,'122n')

		with open(outputfile,'w') as file:
			for i in range(len(sf)):
				file.write(sf[i])
				#print(self._userdata[i+1][1]) 
				#print(type(self._userdata[i+1][1])) 
				salary = self._userdata[i+1][1]
				sf.extend(self.caculator(salary,Config))
				#print(t)
			print(sf)

			



c = Config(configfile)
d = UserData(userdatafile)

d.dumpptofile(outputfile,c)

'''








