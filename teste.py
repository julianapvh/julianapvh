import pygal

pie = pygal.Pie()
pie.title = "Time Spent on Social Networks"
pie.add("Twitter",47)
pie.add("Facebook",23)
pie.add("Instagram",30)

pie.render_in_browser()