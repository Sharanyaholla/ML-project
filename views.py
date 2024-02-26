from django.shortcuts import render
def microbes(request):
    if(request.method=="POST"):
        data=request.POST
        serialno=data.get('textserialno')
        solidity=data.get('textsolidity')
        eccentricity=data.get('texteccentricity')
        equidiameter=data.get('textequidiameter')
        extrema=data.get('textextrema')
        filledarea=data.get('textfilledarea')
        extent=data.get('textextent')
        orientation=data.get('textorientation')
        eulernumber=data.get('texteulernumber')
        boundingbox1=data.get('textboundingbox1')
        boundingbox2=data.get('textboundingbox2')
        boundingbox3=data.get('textboundingbox3')
        boundingbox4=data.get('textboundingbox4')
        convexhull1=data.get('textconvexhull1')
        convexhull2=data.get('textconvexhull2')
        convexhull3=data.get('textconvexhull3')
        convexhull4=data.get('textconvexhull4')
        majoraxislength=data.get('textmajoraxislength')
        minoraxislength=data.get('textminoraxislength')
        perimeter=data.get('textperimeter')
        convexarea=data.get('textconvexarea')
        centroid1=data.get('textcentroid1')
        centroid2=data.get('textcentroid2')
        area=data.get('textarea')
        raddi=data.get('textraddi')if('buttonpredict' in request.POST):
            import pandas as pd
            path="C:\\Users\\shara\\OneDrive\\Desktop\\Project\\train_dataset.csv"
            data=pd.read_csv(path)
            inputs=data.drop(['microorganisms'],'columns')
            output=data['microorganisms']
            
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)

            from sklearn.neighbors import KNeighborsClassifier
            model=KNeighborsClassifier(n_neighbors=13)
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            result=model.predict([[float(serialno),float(solidity),float(eccentricity),float(equidiameter),float(extrema),float(filledarea),float(extent),float(orientation),float(eulernumber),float(boundingbox1),float(boundingbox2),float(boundingbox3),float(boundingbox4),float(convexhull1),float(convexhull2),float(convexhull3),float(convexhull4),float(majoraxislength),float(minoraxislength),float(perimeter),float(convexarea),float(centroid1),float(centroid2),float(area),float(raddi)]])
            return render(request,'microbes.html',context={'result':result})
    return render(request,'microbes.html')