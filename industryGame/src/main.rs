mod turn_loop;
use std::sync::Mutex;
static GAME_FAILED: Mutex<bool> = Mutex::new(false);

fn main() {
    println!("Hello, world!");
    while *GAME_FAILED.lock().unwrap() != true {
        turn_loop::turn();
    }
}
