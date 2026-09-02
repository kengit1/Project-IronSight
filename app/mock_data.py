"""
Gym Machine Exercise Database
------------------------------
Each entry contains:
  - equipment: the machine/exercise name
  - primary_muscle: the main muscle group targeted
  - academic_info: a short coaching tip for correct form
  - video_url: a MuscleWiki page with an animated form-demo video

Note: the "null" checklist item from your source list wasn't a real
exercise, so it's been left out of this database.
"""

MOCK_DATABASE = {
    "Arm Curl Machine": {
        "equipment": "Arm Curl Machine",
        "primary_muscle": "Biceps Brachii",
        "academic_info": "Keep your upper arms pinned to the pad throughout the movement — letting your elbows drift forward turns the curl into a shoulder exercise instead of a biceps one.",
        "video_url": "https://musclewiki.com/exercise/machine-bicep-curl",
         "visual" : "visaulDataset/1614.gif"
    },
    "Chest Fly Machine": {
        "equipment": "Chest Fly Machine (Pec Deck)",
        "primary_muscle": "Pectoralis Major",
        "academic_info": "Keep a slight bend in your elbows and squeeze your chest at the peak of the movement rather than relying on momentum to bring the handles together.",
        "video_url": "https://musclewiki.com/exercise/machine-pec-fly" ,
        "visual" : "visaulDataset/0596.gif"
    },
    "Chest Press Machine": {
        "equipment": "Chest Press Machine",
        "primary_muscle": "Pectoralis Major",
        "academic_info": "Adjust the seat so the handles line up with mid-chest height, and stop just short of locking out your elbows to keep tension on the pecs.",
        "video_url": "https://musclewiki.com/exercise/machine-chest-press" ,
        "visual" : "visaulDataset/0577.gif"
    },
    "Chinning Dipping": {
        "equipment": "Assisted Chin-Up / Dip Machine",
        "primary_muscle": "Latissimus Dorsi (chin-up) / Triceps (dip)",
        "academic_info": "Choose an assistance weight that lets you complete full reps with control — the goal is to gradually reduce assistance over time, not to rely on it forever.",
        "video_url": "https://musclewiki.com/exercise/machine-assisted-chin-up" ,
        "visual" : "visaulDataset/0572.gif"
    },
    "Lat Pull Down": {
        "equipment": "Lat Pull Down",
        "primary_muscle": "Latissimus Dorsi (Lats)",
        "academic_info": "Focus on pulling with your elbows and keeping your chest up to avoid upper-trapezius dominance.",
        "video_url": "https://musclewiki.com/exercises/back/lat-pulldown" ,
        "visual" : "visaulDataset/0818.gif"
    },
    "Lateral Raises Machine": {
        "equipment": "Lateral Raise Machine",
        "primary_muscle": "Lateral Deltoid",
        "academic_info": "Raise with a slight bend in your elbows and stop around shoulder height — going higher shifts the work onto your traps instead of your shoulders.",
        "video_url": "https://musclewiki.com/exercise/machine-standing-lateral-raise",
        "visual" : "visaulDataset/0584-LateralRaise.gif"
    },
    "Leg Extension": {
        "equipment": "Leg Extension Machine",
        "primary_muscle": "Quadriceps",
        "academic_info": "Extend your legs fully but avoid slamming into lockout, and control the negative on the way down instead of letting the weight stack drop.",
        "video_url": "https://musclewiki.com/exercise/machine-leg-extension" ,
        "visual" : "visaulDataset/0585-LegExtension.gif"
    },
    "Leg Press": {
        "equipment": "Leg Press Machine",
        "primary_muscle": "Quadriceps (with Glutes & Hamstrings)",
        "academic_info": "Never let your lower back round off the pad at the bottom of the rep — stop the descent before that happens, even if it limits your range of motion.",
        "video_url": "https://musclewiki.com/exercise/machine-leg-press" ,
        "visual" : "visaulDataset/1463-LegPress.gif"
    },
    "Leg Curl Machine": {
        "equipment": "Leg Curl Machine (Seated)",
        "primary_muscle": "Hamstrings",
        "academic_info": "Curl through a full range of motion and pause briefly at full contraction — most people cut the rep short and lose out on hamstring engagement.",
        "video_url": "https://musclewiki.com/exercise/seated-leg-curl" ,
        "visual" : "visaulDataset/0599-LegCurl.gif"
    },
    "Seated Cable Rows": {
        "equipment": "Seated Cable Row Machine",
        "primary_muscle": "Middle Back (Rhomboids & Lats)",
        "academic_info": "Drive your elbows back and squeeze your shoulder blades together at the end of each pull instead of leaning your torso back to move the weight.",
        "video_url": "https://musclewiki.com/exercise/machine-seated-cable-row" ,
        "visual" : "visaulDataset/0239-SeatedRow.gif"
    },
    "Shoulder Press Machine": {
        "equipment": "Shoulder Press Machine",
        "primary_muscle": "Anterior & Lateral Deltoids",
        "academic_info": "Press directly overhead without arching your lower back off the pad, and stop just shy of locking your elbows at the top.",
        "video_url": "https://www.muscleandstrength.com/exercises/machine-shoulder-press" ,
        "visual" : "visaulDataset/2318-ShoulderPress.gif"
    },
    "Smith Machine Bench Press": {
        "equipment": "Smith Machine",
        "primary_muscle": "Varies by exercise (Chest, Shoulders, Legs, etc.)",
        "academic_info": "The bar path is fixed vertically, so position your body — not the bar — to match a natural pressing or squatting path, and always use the safety hooks.",
        "video_url": "https://musclewiki.com/exercise/smith-machine-bench-press" ,
        "visual" : "visaulDataset/1308-WideGripSmith.gif"
    },
}