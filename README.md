small pieces of code that could be useful

JNDI
https://docs.oracle.com/javase/tutorial/jndi/ops/index.html

https://docs.oracle.com/javase/jndi/tutorial/beyond/env/index.html

LDAP Setup
https://docs.oracle.com/javase/tutorial/jndi/software/content.html

calculate lines of code in repository :)

git ls-files | while read f; do git blame -w --line-porcelain -- "$f" | grep -I '^author '; done | sort -f | uniq -ic | sort -n
