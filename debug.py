from aerofiles.igc import Reader
from opensoar.competition.soaringspot import get_info_from_comment_lines
from opensoar.task.trip import Trip

with open('./igc-files/LeMans_KB.igc', 'r') as f:
    parsed_igc_file = Reader().read(f)

# example.igc comes from soaringspot and contains task inforamtion
task, _, _ = get_info_from_comment_lines(parsed_igc_file)
_, trace = parsed_igc_file['fix_records']

trip = Trip(task, trace)
task_distance_covered = sum(trip.distances)