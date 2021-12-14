## presentaciones_web
### Proyecto Presentaciones Web a cargo del profesor Fabián Abarca

1. Para ejecutarlo en forma de video : 

    manim -pql scene.py Plantilla
   
2. Para ejecutarlo en forma de presentación : 

    manim -qh scene.py  
    manim-presentation Plantilla
    
3. Para ajustar la pantalla completa, reduciendo la calidad : 

    manim_presentation --fullscreen example
 
4. Para guardar cada scene como un gif : 

    manim -ql --save_as_gif scene.py
