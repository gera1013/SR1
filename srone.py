from gl import Render, color

render = Render()

next = True
vp_continue = False
clear_continue = False
vertex_color_continue = False
vertex_continue = False

while next:
    choice = int(input("\n1. Punto\n2. Salir\nIngrese el número de la acción a realizar: "))

    if choice == 1:
        print("\nWINDOW - Ingrese números enteros")
        width = int(input("Ancho de la ventana: "))
        height = int(input("Alto de la ventana: "))

        render.glCreateWindow(width, height)

        while not vp_continue:
            print("\nVIEWPORT - Ingrese números enteros")
            vp_x = int(input("Punto inicial en x: "))
            vp_y = int(input("Punto inicial en y: "))
            vp_width = int(input("Ancho del viewport: "))
            vp_height = int(input("Alto del viewport: "))

            vp_continue = render.glViewPort(vp_x, vp_y, vp_width, vp_height)

            if not vp_continue:
                print("\nLos valores ingresados exceden el tamaño de la ventana")

        while not clear_continue:
            print("\nCLEAR - Ingrese números de tipo flotante entre 0 y 1")
            clear_color_r = float(input("Ingrese el valor de R: "))
            clear_color_g = float(input("Ingrese el valor de G: "))
            clear_color_b = float(input("Ingrese el valor de B: "))

            if clear_color_r > 1 or clear_color_r < 0 or clear_color_g > 1 or clear_color_g < 0 or clear_color_b > 1 or clear_color_b < 0:
                print("\n Los valores ingresados no son válidos, ingrese números entre 0 y 1")
            else:
                clear_continue = True
                render.glClearColor(clear_color_r, clear_color_g, clear_color_b)
                render.glClear()
        
        while not vertex_color_continue:
            print("\nVERTEX COLOR - Ingrese números de tipo flotante entre 0 y 1")
            vertex_color_r = float(input("Ingrese el valor de R: "))
            vertex_color_g = float(input("Ingrese el valor de G: "))
            vertex_color_b = float(input("Ingrese el valor de B: "))

            if vertex_color_r > 1 or vertex_color_r < 0 or vertex_color_g > 1 or vertex_color_g < 0 or vertex_color_b > 1 or vertex_color_b < 0:
                print("\n Los valores ingresados no son válidos, ingrese números entre 0 y 1")
            else:
                render.glColor(vertex_color_r, vertex_color_g, vertex_color_b)
                vertex_color_continue = True
        
        while not vertex_continue:
            print("\nVERTEX - Ingrese números de tipo flotante entre -1 y 1")
            vertex_x = float(input("Ingrese el valor para x: "))
            vertex_y = float(input("Ingrese el valor para y: "))

            if vertex_x > 1 or vertex_x < -1 or vertex_y > 1 or vertex_y < -1:
                print("\n Los valores ingresados no son válidos, ingrese números entre -1 y 1")
            else:
                render.glVertex(vertex_x, vertex_y)
                vertex_continue = True

        input("\nPRESIONE ENTER PARA DIBUJAR")

        print("\nDibujando...")
        render.glFinish()

        print("\nFinalizado! El archivo se encuentra en la misma carpeta que este, bajo el nombre de 'SR1.bmp'\n")
    
    elif choice == 2:
        next = False