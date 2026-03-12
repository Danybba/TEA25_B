import pygal

pie = pygal.Pie()

pie.title = "Time spend on social media"
pie.add("Twitter",47)
pie.add("Facebook", 35)
pie.add("Instagram", 18)

pie.render_in_browser()

