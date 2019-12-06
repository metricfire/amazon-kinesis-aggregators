build-docker:
	docker build . -t metricfire/kinesis-agg
aws:
	docker build . --no-cache -t 540840259067.dkr.ecr.us-east-1.amazonaws.com/metricfire/kinesis-aggregator
	docker push 540840259067.dkr.ecr.us-east-1.amazonaws.com/metricfire/kinesis-aggregator
