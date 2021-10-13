else:
                            preve_node = current.prev
                            next_node = current.next
                            preve_node.next = next_node
                            next_node.prev = preve_node
                            current.prev = None
                            current.next = None
                            break