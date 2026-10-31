def get_batch_generator(data, batch_size):
    """Yields successive batch_size chunks from data."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def main():
    data = list(range(10))
    batch_size = 4
    epochs = 2

    # Loop through the training epochs
    for epoch in range(1, epochs + 1):
        print(f"--- Epoch {epoch} ---")

        # A fresh generator instance must be created for each epoch
        batch_gen = get_batch_generator(data, batch_size)

        for batch in batch_gen:
            print(f"Batch: {batch}")
        print()

if __name__ == "__main__":
    main()
