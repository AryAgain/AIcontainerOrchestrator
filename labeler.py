import pandas as pd

# Thresholds
CPU_HIGH_THRESHOLD = 70  
CPU_LOW_THRESHOLD = 20  
MEMORY_HIGH_THRESHOLD = 70 
MEMORY_LOW_THRESHOLD = 20

def label_utilization(row):
    cpu = row['cpu']
    memory = row['ram']
    
    if cpu >= CPU_HIGH_THRESHOLD or memory >= MEMORY_HIGH_THRESHOLD:
        return 'H'
    elif cpu <= CPU_LOW_THRESHOLD and memory <= MEMORY_LOW_THRESHOLD:
        return 'L'
    else:
        return 'M'

def main():
    
    df = pd.read_csv('utilization.csv')
    df['label'] = df.apply(label_utilization, axis=1)
    
    df.to_csv('labeled_utilization.csv', index=False)
    print("Labeled data has been written to 'labeled_utilization.csv'")

if __name__ == "__main__":
    main()