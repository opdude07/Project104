import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(
            img,
            "Sun",
             (70,80),
             cv2.FONT_HERSHEY_TRIPLEX,
             2,
             (0,255,255)

            ) 
cv2.putText(
            img,
            "Mercury",
             (117,238),
             cv2.FONT_HERSHEY_COMPLEX,
             0.4,
             (255,150,255)

            )   
cv2.putText(
            img,
            "Venus",
             (188,260),
             cv2.FONT_HERSHEY_TRIPLEX,
             0.5,
             (255,0,255)
             
            )  
cv2.putText(
            img,
            "Earth",
             (286,262),
             cv2.FONT_HERSHEY_TRIPLEX,
             0.5,
             (255,0,0)
             
            )           
cv2.putText(
            img,
            "Mars",
             (385,250),
             cv2.FONT_HERSHEY_TRIPLEX,
             0.5,
             (0,255,0)
             
            )    
cv2.putText(
            img,
            "Jupiter",
             (490,260),
             cv2.FONT_HERSHEY_TRIPLEX,
             1.1,
             (0,0,255)
             
            )     
cv2.putText(
            img,
            "Saturn",
             (740,300),
             cv2.FONT_HERSHEY_TRIPLEX,
             0.8,
             (155,155,150)
             
            )     
cv2.putText(
            img,
            "Uranus",
             (960,300),
             cv2.FONT_HERSHEY_TRIPLEX,
             0.6,
             (55,0,255)
             
            )    
cv2.putText(
            img,
            "Neptune",
             (1101,290),
             cv2.FONT_HERSHEY_TRIPLEX,
             0.7,
             (255,200,255)
             
            )    
cv2.imshow("output",img)
cv2.waitKey(0)