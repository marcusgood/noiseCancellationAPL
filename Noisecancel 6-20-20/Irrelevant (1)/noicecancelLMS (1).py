import padasip as pa

def lms_loop(wave_measure, output_goal):

    lms_filter = pa.filters.FilterLMS(3, mu=1.0)

    for . . .    #How to loop enough times to get close enough to desired output?
    
        x = wave_measure
    
        y = lms_filter.predict(x)
    
        pass
    
        d = output_goal
        
        lms_filter.adapt(d, x)
    
    
    
    