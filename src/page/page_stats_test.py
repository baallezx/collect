import page
import page_stats as pgs

tp = page.page("http://ccs.com/index")
tp.data = "this is a string\nit has some data in it.\n\nscoobydoo!\n\n\n:)\n\n"

tps = pgs.page_stats(tp)
