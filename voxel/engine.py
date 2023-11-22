import sys
from moderngl import Context
import moderngl
import pygame

from settings import BACKGROUND_COLOR


class Engine:
    ctx: Context
    clock: pygame.time.Clock
    delta_time: int
    time: float
    is_running: bool

    def __init__(self, window_resolution: tuple[float, float]) -> None:
        pygame.init()

        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )

        # window resolution and opengl context
        pygame.display.set_mode(
            window_resolution, flags=pygame.OPENGL | pygame.DOUBLEBUF
        )
        self.ctx = moderngl.create_context()

        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND)
        self.ctx.gc_mode = "auto"  # automatic garbage collection

        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True

    # update object states
    def update(self) -> None:
        self.delta_time = self.clock.tick()
        self.time = pygame.time.get_ticks() * 0.001

        # show fps
        pygame.display.set_caption(f"{self.clock.get_fps() :.0f}")

    def render(self) -> None:
        self.ctx.clear(color=BACKGROUND_COLOR)
        pygame.display.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event == pygame.K_ESCAPE
            ):
                self.is_running = False

    def run(self) -> None:
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()
