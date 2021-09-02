from multiprocessing import cpu_count


global_args = {
    "output_dir": "models",
    "best_model_dir": "models/best_model",
    "cache_dir": "cache_dir/",
    "config": {},
    "fp16": False, #False
    "fp16_opt_level": "O2", #02
    "max_seq_length": 128, #128, 512 256
    "train_batch_size": 16, #8 16
    "gradient_accumulation_steps": 16, #8 16
    "eval_batch_size": 8, #8
    "num_train_epochs": 3, #8, 3
    "weight_decay": 0,
    "learning_rate": 1e-5, #1e-4 1e-5 1e-8 3e-5 0.01 4e-5 1e-3 3e-5 5e-5
    "adam_epsilon": 1e-8,
    "warmup_ratio": 0.06,
    "warmup_steps": 0,
    "max_grad_norm": 1.0,
    "do_lower_case": False, #False
    "logging_steps": 50,
    "save_steps": 2000, #2000 1000000000
    "save_optimizer_and_scheduler": True,
    "no_cache": True, #False
    "no_save": False,
    "save_model_every_epoch": True, #True False
    "evaluate_during_training": True,
    "evaluate_during_training_steps": 2000,
    "evaluate_during_training_verbose": True,
    "use_cached_eval_features": False,
    "save_eval_checkpoints": True, #True
    "tensorboard_dir": None,
    "overwrite_output_dir": True, #True
    "reprocess_input_data": True,
    "process_count": cpu_count() - 2 if cpu_count() > 2 else 1,
    "n_gpu": 1,
    "use_multiprocessing": True,
    "silent": False,
    # "wandb_project": "continuous-learner",
    "wandb_project": None,
    # "wandb_entity":'tosi-n',
    "wandb_kwargs": {},
    "use_early_stopping": True,
    "early_stopping_patience": 3,
    "early_stopping_delta": 0,
    "early_stopping_metric": "eval_loss",
    "early_stopping_metric_minimize": True,
    "manual_seed": 123,
    "encoding": None,
}