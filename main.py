file = open('text.txt')
text = file.read()
file.close()


repl = {'&' : '&amp;','<' : '&lt;', '>' : '&gt;', '\"' : '&quot;', '\'' : '&apos;' }
for i in repl.keys(): text = text.replace(i, repl[i])
for i in ['&amp;', '&lt;', '&gt;', '&quot;', '&apos;']:
    text = text.replace(i, '<sss>' + i + '</sss>')


#vars_open = [' (', ' [']
#vars_closed = [') ', '] ']
#special_open = ['.']
#special_close = ['('] #, ');'


s_defs = ['(', ')', '[', ']', '{', '}']     #deef loop call
#c_classes = ['int', 'vector', 'set', 'map']     #c++
#cc_classes = {'_<class>set</class>' : '_set', '_<class>map</class>' : '_map'}    #c++
#c__classes = ['unordered_set', 'unordered_map']
#c_defs = ['main', 'readInt', 'writeInt', 'readChar', 'chng']    #c++
p_defs = ['print(', '.keys', '.read', 'len(', 'ord(', 'sorted(',
          'range(', 'lambda', '.append',
          'perm', 'get_new_index', 'back_index', 'coding']
s_special = ['+', '=', '-', '*', '%',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'else ', 'if ', 'elif ', 'for ', 'while ', 'in ',
             'return']   #sss op x m '#include'
s_vars = [',', ';\n', ':']

for i in p_defs: text = text.replace(i, '<def>' + i + '</def>')
#for i in special_open: text = text.replace(i, i + '<sss>')
#for i in special_close: text = text.replace(i, '</sss>' + i)
#for i in vars_open: text = text.replace(i, i + '<var>')
#for i in vars_closed: text = text.replace(i, '</var>' + i)
for i in s_vars: text = text.replace(i, '<var>' + i + '</var>')
#for i in c_classes: text = text.replace(i, '<class>' + i + '</class>')
#for i in cc_classes.keys(): text = text.replace(i, cc_classes[i])
#for i in c_defs: text = text.replace(i, '<def>' + i + '</def>')
for i in s_special: text = text.replace(i, '<sss>' + i + '</sss>')
for i in s_defs: text = text.replace(i, '<def>' + i + '</def>')
#for i in c__classes: text = text.replace(i, '<class>' + i + '</class>')


new_file = open('edited.txt', 'w+')
new_file.write(text)
new_file.close()


print('''
                      ____...                                  
             .-"--"""".__    `.                                
            |            `    |                                
  (         `._....------.._.:          
   )         .()''        ``().                                
  '          () .=='  `===  `-.         
   . )       (         g)                                
    )         )     /        J          
   (          |.   /      . (                                  
   $$         (.  (_'.   , )|`                                 
   ||         |\`-....--'/  ' \                                
  /||.         \\ | | | /  /   \.                              
 //||(\         \`-===-'  '     \o.                            
.//7' |)         `. --   / (     OObaaaad888b.                 
(<<. / |     .a888b`.__.'d\     OO888888888888a.               
 \  Y' |    .8888888aaaa88POOOOOO888888888888888.              
  \  \ |   .888888888888888888888888888888888888b              
   |   |  .d88888P88888888888888888888888b8888888.             
   b.--d .d88888P8888888888888888a:f888888|888888b             
   88888b 888888|8888888888888888888888888\8888888
    ''')