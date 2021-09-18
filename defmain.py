def main():
    pygame.init()
    display = (display_width ,display_length)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


    max_distance = 100
    
    gluPerspective(45, (display[0]/display[1]), 0.1, max_distance)

    glTranslatef(0,0, -40)



    x_move = 0
    y_move = 0

    cur_x = 0
    cur_y = 0

    game_speed = 2
    direction_speed = 2

    

    cube_dict = {}

    for x in range(50):
        cube_dict[x] =set_vertices(max_distance)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = direction_speed
                if event.key == pygame.K_RIGHT:
                    x_move = -1*direction_speed

                if event.key == pygame.K_UP:
                    y_move = -1*direction_speed
                if event.key == pygame.K_DOWN:
                    y_move = direction_speed


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0


                    

        


        x = glGetDoublev(GL_MODELVIEW_MATRIX)
  

        
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        
        cur_x += x_move
        cur_y += y_move
        

                    
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glTranslatef(x_move,y_move,game_speed)



        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])

        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                new_max = int(-1*(camera_z-(max_distance*2)))
                cube_dict[each_cube] = set_vertices(new_max,int(camera_z-max_distance), cur_x, cur_y)

                

            
        pygame.display.flip()

