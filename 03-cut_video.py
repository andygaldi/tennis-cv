from google.cloud import videointelligence_v1 as vi


def detect_shot_changes(video_uri: str) -> vi.VideoAnnotationResults:
    video_client = vi.VideoIntelligenceServiceClient()
    features = [vi.Feature.SHOT_CHANGE_DETECTION]
    request = vi.AnnotateVideoRequest(input_uri=video_uri, features=features)

    print(f'Processing video: "{video_uri}"...')
    operation = video_client.annotate_video(request)

    return operation.result().annotation_results[0]  # Single video


def print_video_shots(results: vi.VideoAnnotationResults):
    shots = results.shot_annotations
    print(f" Video shots: {len(shots)} ".center(40, "-"))
    for i, shot in enumerate(shots):
        t1 = shot.start_time_offset.total_seconds()
        t2 = shot.end_time_offset.total_seconds()
        print(f"{i+1:>3} | {t1:7.3f} | {t2:7.3f}")


if __name__ == "__main__":
    video_uri = "gs://slow-motion-videos/NDjokovicFH.mp4"
    results = detect_shot_changes(video_uri)
    print_video_shots(results)
