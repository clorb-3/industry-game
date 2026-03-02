/*mod turn_loop;
use std::{fs::OpenOptions, sync::Mutex};
use winit::event_loop::EventLoop;
static GAME_FAILED: Mutex<bool> = Mutex::new(false);

fn main() {
    println!("Hello, world!");
    while *GAME_FAILED.lock().unwrap() != true {
        turn_loop::turn();
    }
}
*/

// windowed text rendering
/*
use winit::application::ApplicationHandler;
use winit::event::WindowEvent;
use winit::event_loop::{ActiveEventLoop, ControlFlow, EventLoop};
use winit::window::{Window, WindowId};

#[derive(Default)]
struct App {
    window: Option<Window>,
}

impl ApplicationHandler for App {
    fn resumed(&mut self, event_loop: &ActiveEventLoop) {
        let window = event_loop
            .create_window(Window::default_attributes())
            .unwrap();

        window.request_redraw();

        self.window = Some(window);
    }

    fn window_event(
        &mut self,
        event_loop: &ActiveEventLoop,
        window_id: WindowId,
        event: WindowEvent,
    ) {
        match event {
            WindowEvent::CloseRequested => {
                println!("Exiting application");
                event_loop.exit();
            }
            WindowEvent::RedrawRequested => {
                self.window.as_ref().unwrap().request_redraw();
            }
            _ => (),
        }
    }
}

fn main() {
    let event_loop = EventLoop::new().unwrap();

    event_loop.set_control_flow(ControlFlow::Poll);

    let mut app = App::default();
    event_loop.run_app(&mut app);
}
*/

impl<'a> ApplicationHandler for App<'a> {
    fn resumed(&mut self, event_loop: &winit::event_loop::ActiveEventLoop) {
        let window = event_loop
            .create_window(Window::default_attributes())
            .unwrap();

        // softbuffer context & surface store references
        let context = unsafe { softbuffer::Context::new(&window).unwrap() };
        let surface = unsafe { softbuffer::Surface::new(&context, &window).unwrap() };

        window.request_redraw();

        self.window = Some(window);
        self.context = Some(context);
        self.surface = Some(surface);
    }

    fn window_event(
        &mut self,
        event_loop: &winit::event_loop::ActiveEventLoop,
        _id: WindowId,
        event: WindowEvent,
    ) {
        match event {
            WindowEvent::CloseRequested => event_loop.exit(),

            WindowEvent::RedrawRequested => {
                let window = self.window.as_ref().unwrap();
                let surface = self.surface.as_mut().unwrap();

                let size = window.inner_size();
                surface.resize(size.width, size.height).unwrap();

                let mut buffer = surface.buffer_mut().unwrap();
                buffer.fill(0x002020FF); // blue
                buffer.present().unwrap();
            }

            _ => {}
        }
    }
}
