## Data Summary:

__Technological process:__
- *Rougher feed* — raw material
- *Rougher additions (or reagent additions)* — flotation reagents: Xanthate, Sulphate, Depressant
- *Xanthate* — promoter or flotation activator;
- *Sulphate* — sodium sulphide for this particular process;
- *Depressant* — sodium silicate.
- *Rougher process* — flotation
- *Rougher tails* — product residues
- *Float banks* — flotation unit
- *Cleaner process* — purification
- *Rougher Au* — rougher gold concentrate
- *Final Au* — final gold concentrate

__Parameters of stages:__
- *air amount* — volume of air
- *fluid levels*
- *feed size* — feed particle size
- *feed rate*

- __Possible values for `[stage]`__:
- *rougher* — flotation
- *primary_cleaner* — primary purification
- *secondary_cleaner* — secondary purification
- *final* — final characteristics

__Possible values for `[parameter_type]`:__
- *input* — raw material parameters
- *output* — product parameters
- *state* — parameters characterizing the current state of the stage
- *calculation* — calculation characteristics

__Recovery calculation:__
You need to simulate the process of recovering gold from gold ore.
- *C* — share of gold in the concentrate right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
- *F* — share of gold in the feed before flotation (for finding the rougher concentrate recovery)/in the concentrate right after flotation (for finding the final concentrate recovery)
- *T* — share of gold in the rougher tails right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)

## Goal:

Prepare a prototype of a machine learning model for Zyfra. The company develops efficiency solutions for heavy industry.

The model should predict the amount of gold recovered from gold ore. You have the data on extraction and purification.

The model will help to optimize the production and eliminate unprofitable parameters.

You need to:
1. Prepare the data;
2. Perform data analysis;
3. Develop and train a model.

## Libraries used:

sklearn, pandas, numpy, matlibplot

[:snake: Jupyter Notebook](./Integrated_Project_2.ipynb)