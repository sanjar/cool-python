from resolver import Resolver
r = Resolver()
r('google.com')
r('pluralsight.com')

r.timeit("r('google.com')")
r.timeit("r('google.com')")
r.timeit("r('pluralsight.com')")