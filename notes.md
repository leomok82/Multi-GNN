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

8. Inference

python main.py --inference --data data --model gin --emlps --reverse_mp --ports  --unique_name "edge"

9. Remove this in inference.py
comment out the whole if statement from 64 to 68 (args.avg_tps does not exist)
10.  remove this in inference.py
precrec=True

11. in train_util.py, evaluate_hetero function, add saving preds to csv
    unique_edge_id = batch['node', 'to', 'node'].edge_attr[:, 0].detach().cpu()