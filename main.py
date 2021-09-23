import pygame, threading, time
import interface, func

def main():
    pygame.display.set_caption("Multithreading Bouncing Balls")
    pygame.display.init()

    ### Display ###
    close = False
    clock = pygame.time.Clock()

    func.make_ball()
    threads = list()

    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for _ in range (len(func.balls)):
                    if len(func.balls) > 0:
                        func.balls.pop(-1)
                close = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if interface.button_add_thread.collidepoint((pos[0], pos[1] - interface.DISP_THREAD_HEIGHT_BORDER)):
                    func.make_ball()
                elif interface.button_add_x10_thread.collidepoint((pos[0], pos[1] - interface.DISP_THREAD_HEIGHT_BORDER)):
                    for _ in range(10):
                        func.make_ball()
                elif interface.button_remove_thread.collidepoint((pos[0], pos[1] - interface.DISP_THREAD_HEIGHT_BORDER)):
                    if len(func.balls) > 0:
                        func.balls.pop(-1)
                elif interface.button_remove_all_thread.collidepoint((pos[0], pos[1] - interface.DISP_THREAD_HEIGHT_BORDER)):
                    for _ in range (len(func.balls)):
                        if len(func.balls) > 0:
                            func.balls.pop(-1)
                elif interface.button_close.collidepoint((pos[0], pos[1] - interface.DISP_THREAD_HEIGHT_BORDER)):
                    for _ in range (len(func.balls)):
                        if len(func.balls) > 0:
                            func.balls.pop(-1)
                    close = True
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    func.make_ball()
                if event.key == pygame.K_x:
                    for _ in range(10):
                        func.make_ball()
                if event.key == pygame.K_DELETE:
                    if len(func.balls) > 0:
                        func.balls.pop(-1)

        ### Threads Ball Movement ###
        new_threads_needed = len(func.balls) - len(threads)
        for _ in range(new_threads_needed):
            thread = func.threads_balls()
            thread.start()
            threads.append(thread)

        if new_threads_needed < 0:
            threads[-1].kill = True
            threads.pop(-1)

        interface.s.fill(interface.grey)
        ### Draw Balls ###
        for ball in func.balls:
            pygame.draw.circle(interface.s, ball.color, [ball.x, ball.y], 25)
        
        ### Display Threads Counter ###
        interface.display_threads(len(threads))

        ass = interface.font_1.render("Dev.: Fábio R. P. Nunes", 10, interface.light_grey_2)
        interface.s.blit(ass, (630, 580))
        interface.window.blit(interface.s, (interface.DISP_THREAD_WIDTH_BORDER, 0))
        
        pygame.display.update()
        clock.tick(240)

    pygame.display.quit()

if __name__ == "__main__":
    main()