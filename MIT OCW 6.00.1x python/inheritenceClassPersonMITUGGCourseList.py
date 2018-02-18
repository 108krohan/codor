import datetime

class Person(object):

    def __init__(self, name):
        #create a person with name name
        self.name = name
        try :
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except :
                self.lastName = name
        self.birthday = None

    def getLastName(self):
        #return self's last name
        return self.lastName

    def setBirthday(self, birthDate):
        #assume birthDate is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate

    def getAge(self):
        #assumes that self's birthday has been set, returns self's
        #current age in days
        assert self.birthday is not None
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
        greater than other's name, and False otherwise"""
        print 'eaating shit from Person'
        if self.lastName == other.lastName :
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        #return self's name
        return self.name

##me = Person ('Rohan Kumar')
##him = Person ('John Guttag')
##her = Person ('Madonna')
##print him
##print him.getLastName()
##him.setBirthday(datetime.date(1964,8,4))
##her.setBirthday(datetime.date(1958,8,16))
###him.birthday = '8/4/61'/TypeError Evil
##print her.getAge()
##print him.getAge()
##print him < her
##print me < her
##pList = [me, him, her]
##print 'The people in pList are : '
##for p in pList :
##    print '\t' + str(p)
##
##pList.sort()
##print 'The people in pList are : '
##for p in pList :
##    print ' ' + str(p)


class MITPerson ( Person ):
    nextIDnum = 0  #class variable
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIDnum
        MITPerson.nextIDnum += 1

    def getIDnum(self):
        return self.idNum

    def __lt__(self,other):
        print 'eating shit from MITPerson ', self.idNum
        return self.idNum < other.idNum

    def isStudent(self):
        return type(self) == UG or type(self) == G


##p1 = MITPerson ('Barbara Beaver')
##print p1, p1.getIDnum()
##p2 = MITPerson ('Sue Yuan')
##p3 = MITPerson ('Sue Yuan')
##print p2, p2.getIDnum()
##print p3, p3.getIDnum()
##
##p4 = Person ('Rohan Kumar')
##print 'p1 < p2 = ', p1 < p2     #comparing IDnums
##print 'p3 < p2 = ', p3 < p2
####Suppose I want to compare names of the Persons
##print '__lt__(p1,p2) = ', Person.__lt__(p1,p2)
##
##
##print 'p1 == p4 = ', p1 == p4
##print 'p4 < p3 = ', p4 < p3 #name wise
####print 'p3 < p4 = ', p3 < p4 #AttributeError p4 is a Person not an MITPerson
##print 'p3 < p4 = ', Person.__lt__(p3,p4)    ##name wise

class UG(MITPerson):

    def  __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None

    def setYear(self, year):
        if year > 5 :
            raise OverflowError("Too Many")
        self.year = year

    def getYear(self):
        return self.setYear(int(raw_input('Enter the year of study : ')))

##ug1 = UG ('Tomahok Doe')
##ug2 = UG ('Tomahok Doe')
##p3 = MITPerson ('Sue Yuan')
##print ug1
##print ug1 < p3
##print ug2 < ug1
##print ug1 is ug2
##ug1.getYear()

class G(MITPerson):
    pass

g1 = G('Mitch Peabody')


""" Try type(g1)
type(g1) == G --> True """

class CourseList(object):

    def __init__(self,number):
        self.number = number
        self.students = []

    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError('Not a student')
        if who in self.students :
            raise ValueError('Duplicate student')
        self.students.append(who)

    def remStudent(self,who):
        try:
            self.students.remove(who)
        except:
            print str(who) + ' not in ' + self.number

    def allStudents(self):
        for s in self.students :
            yield s

    def ugs(self):
        indx = 0
        while indx < len(self.students) :
            if type(self.students[indx]) == UG :
                yield self.students[indx]
            indx += 1

m1 = MITPerson ('Barbara Beaver')
ug1 = UG('John Doe')
ug2 = UG('John Doe')
g1 = G('Mitch Perbody')
g2 = G('Ryan Jackson')
g3 = G('Sarne Cavelake')
SixHundred = CourseList('600')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2) #1
rk = MITPerson('Rohan Kumar')
SixHundred.addStudent(rk)
SixHundred.remStudent(rk)


    
