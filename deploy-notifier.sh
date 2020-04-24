#based on https://cloud.google.com/python/tutorials/getting-started-on-compute-engine

ZONE=us-west1-a

gcloud compute instances create "notifier" \
    --machine-type=f1-micro \
    --metadata-from-file startup-script=startup-script.sh \
    --zone $ZONE \
    --tags http-server

gcloud compute instances get-serial-port-output notifier --zone $ZONE

gcloud compute firewall-rules create default-allow-http-8080 \
    --allow tcp:8080 \
    --source-ranges 0.0.0.0/0 \
    --target-tags http-server \
    --description "Allow port 8080 access to http-server"

gcloud compute instances list
