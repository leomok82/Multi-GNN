1.
```python format_kaggle_files.py /Users/leo/Desktop/AML/data/HI-Small_Trans.csv```
creates file in `/Users/leo/Desktop/AML/data/formatted_transactions.csv`
2.
change data_config.json
3. 
login W&B with API
4.
python main.py --data data  --model gin --save_model --unique_name "small"

5. change this
    parser.add_argument("--unique_name",type=str, help="Unique name under which the model will be stored.")

6. collab -> disable

7. enable mps