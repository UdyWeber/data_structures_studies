#[derive(Clone)]
struct Node {
    value: i64,
    next: Option<Box<Node>>
}


struct LinkedList {
    head: Option<Box<Node>>,
    tail: Option<Box<Node>>,
    length: i64
}

impl LinkedList {
    fn new(value: i64) -> Self {
        let new_node = Node { 
            value: value,
            next: None
        };

        let boxed_node = Box::new(new_node);
        let cloned_boxed_node = boxed_node.clone();

        Self {
            head: Some(boxed_node),
            tail: Some(cloned_boxed_node),
            length: 1
        }
    }

    fn print_list_items(&self) {
        // With as_ref we can get a reference of what's inside the box
        let mut actual_node =  self.head.as_ref();

        while let Some(node) = actual_node {
            println!("Node Value: {}", node.value);
            actual_node = node.next.as_ref();
        }
    }


    fn append(&mut self, value: i64) {
        let new_node = Node { 
            value: value,
            next: None
        };

        let boxed_node = Some(Box::new(new_node));

        if let Some(mut last_node) = self.tail.as_mut(){
            last_node.next = boxed_node.clone();
            self.tail = boxed_node;
        }

        self.length += 1;
    }
}


fn main() {
    let mut linked_list = LinkedList::new(56);
    linked_list.append(5123);
    linked_list.print_list_items();
}