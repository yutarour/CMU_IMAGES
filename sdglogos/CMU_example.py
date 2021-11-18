#there are 2 ways to do this. You can either define app.url or oyu can just directly embed it. 

#first method
#this code will place a unsdg #10 logo onto the canvas at a height of 10 and a width of 10.
app.url = "https://raw.githubusercontent.com/Yaurrdautia/CMU_IMAGES/main/sdglogos/unsdg%2010.png"
Image(app.url,0,0,width=10,height=10)

#second method
#this code will place a unsdg #10 logo onto the canvas at a height of 10 and a width of 10.
Image("https://raw.githubusercontent.com/Yaurrdautia/CMU_IMAGES/main/sdglogos/unsdg%2010.png",0,0,width=10,height=10)
