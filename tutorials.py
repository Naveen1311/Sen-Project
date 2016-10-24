#tutorial hardcode printing code
print '***************TUTORIALS*********************'
print '1.for loop\n2.while loop\n3.if else statements\n'
t=input('Give your option to know the tutorial:')
print '\n'
print '***********************************************'
if t==1:
       print 'A for loop is a repetition control structure that allows you to efficiently write a loop that needs to executes a specific number of times.\n\nThe syntax of a for loop in C programming language is:\n\nfor ( init ; condition ; increment ) { \n statement(s); \n }\n\ninit : The init step is executed first ,it allows to declare and initialize any loop control variables.\n\ncondition : the condition is evaluated. If it is true, the body of the loop is executed.If it is false, the body, of the loop does not execute and the flow of control jumps to the next statement just after the for loop.\n\nincrement: After the body of the for loop executes, the flow of control jumps back up to the increment statement. This statement allows you to update any loop control variables. This statement can be left blank, as long as a semicolon appears after the condition.\n'
       
elif t==2:
        print 'A while loop in C programming repeatedly executes a target statement as long as a given condition is true.\n\nThe syntax of a while loop in C programming language is:\n\nwhile (condition ) { \n statement(s); \n }\n\nHere, statement(s) may be a single statement or a block of statements. The condition may be any expression, and true is any nonzero value. The loop iterates while the condition is true.\n'
        
elif t==3:
        print 'An if statement can be followed by an optional else statement, which executes when the Boolean expression is false.\n\n The syntax of an if...else statement in C programming language is : \n\n if (boolean_expression){\n/*statements will execute if the boolean expression is true*/\n}\nelse{\n/*statements will execute if the boolean expression is false*/\n}\n\nIf the boolean expression evaluates to true, then the if block will be executed,otherwise,the else block will be executed.\n'

print '***************************************************'        
        
        
        
        
        
        
        
        
        
