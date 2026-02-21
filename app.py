import random
import streamlit as st
from dataclasses import dataclass
from typing import List, Dict

# ---------------- Data model ----------------
@dataclass
class Question:
    prompt: str
    options: List[str]
    correct: int

# ---------------- Load pools ----------------
def load_homework_pools() -> Dict[str, List[Question]]:
    hw1 = [
        Question("Antiviral drugs that have become useful are usually associated with which of the following properties?",
                 ["ability to remove all viruses from the infected host",
                  "interference with viral replication",
                  "prevention of the host from becoming infected",
                  "removal of viral proteins",
                  "removal of viral mRNAs"], 1),
        Question("As a result of the lytic cycle, _____.",
                 ["the host cell is not destroyed",
                  "the host cell's DNA is destroyed",
                  "viral ribosomes are produced",
                  "viral DNA is incorporated into host cell DNA",
                  "a prophage is created"], 1),
        Question("Clear patches in cell cultures that indicate sites of virus infection are called",
                 ["colonies", "pocks", "plaques", "prions"], 2),
        Question("Emerging viruses arise by",
                 ["mutation of existing viruses.",
                  "the spread of existing viruses to new host species.",
                  "the spread of existing viruses more widely within their host species.",
                  "mutation of existing viruses, the spread of existing viruses to new host species, and the spread of existing viruses more widely within their host species."], 3),
        Question("In the lysogenic cycle _____.",
                 ["host DNA is destroyed and viral DNA is replicated",
                  "a bacterium replicates without passing viral DNA to its daughter cells",
                  "viral DNA is destroyed and host DNA is replicated",
                  "a bacterium divides once before the lytic cycle is initiated",
                  "viral DNA is replicated along with host DNA"], 4),
        Question("The genetic material of the HIV virus consists of _____.",
                 ["single-stranded DNA", "single-stranded RNA", "double-stranded DNA", "double-stranded RNA", "none of the above"], 1),
        Question("Viral DNA makes mRNA by the process of _____.",
                 ["replication", "infection", "translation", "lysis", "transcription"], 4),
        Question("What is the function of reverse transcriptase?",
                 ["It catalyzes the formation of a polypeptide from an RNA template.",
                  "It catalyzes the formation of DNA from a polypeptide template.",
                  "It catalyzes the formation of RNA from a polypeptide template.",
                  "It catalyzes the formation of RNA from a DNA template.",
                  "It catalyzes the formation of DNA from an RNA template."], 4),
        Question("What is the name given to viruses that are single-stranded RNA that acts as a template for DNA synthesis?",
                 ["retroviruses", "proviruses", "viroids", "bacteriophages", "lytic phages"], 0),
        Question("What is the source of a viral envelope?",
                 ["host cell DNA", "prophages", "provirus", "host cell membrane", "viral glycoproteins"], 3),
    ]

    hw2 = [
        Question("According to the induced fit hypothesis of enzyme catalysis, which of the following is correct?",
                 ["The binding of the substrate depends on the shape of the active site.",
                  "Some enzymes change their structure when activators bind to the enzyme.",
                  "A competitive inhibitor can outcompete the substrate for the active site.",
                  "The binding of the substrate changes the shape of the enzyme's active site.",
                  "The active site creates a microenvironment ideal for the reaction."], 3),
        Question("Besides turning enzymes on or off, what other means does a cell use to control enzymatic activity?",
                 ["cessation of cellular protein synthesis",
                  "localization of enzymes into specific organelles or membranes",
                  "exporting enzymes out of the cell",
                  "connecting enzymes into large aggregates",
                  "hydrophobic interactions"], 1),
        Question("The mathematical expression for the change in free energy of a system is ΔG = ΔH - TΔS. Which of the following is (are) correct?",
                 ["ΔS is the change in enthalpy, a measure of randomness.",
                  "ΔH is the change in entropy, the energy available to do work.",
                  "ΔG is the change in free energy.",
                  "T is the temperature in degrees Celsius."], 2),
        Question("Which of the following best describes enthalpy (H)?",
                 ["the total kinetic energy of a system",
                  "the heat content of a chemical system",
                  "the system's entropy",
                  "the cell's energy equilibrium",
                  "the condition of a cell that is not able to react"], 1),
        Question("Which of the following is an example of cooperativity?",
                 ["the binding of an end product of a metabolic pathway to the first enzyme that acts in the pathway",
                  "one enzyme in a metabolic pathway passing its product to act as a substrate for the next enzyme in the pathway",
                  "a molecule binding at one unit of a tetramer, allowing faster binding at each of the other three",
                  "the effect of increasing temperature on the rate of an enzymatic reaction",
                  "binding of an ATP molecule along with one of the substrate molecules in an active site"], 2),
        Question("Which of the following is true for all exergonic reactions?",
                 ["The products have more total energy than the reactants.",
                  "The reaction proceeds with a net release of free energy.",
                  "The reaction goes only in a forward direction: all reactants will be converted to products, but no products will be converted to reactants.",
                  "A net input of energy from the surroundings is required for the reactions to proceed.",
                  "The reactions are rapid."], 1),
        Question("Which of the following is true of metabolism in its entirety in all organisms?",
                 ["Metabolism depends on a constant supply of energy from food.",
                  "Metabolism depends on an organism's adequate hydration.",
                  "Metabolism uses all of an organism's resources.",
                  "Metabolism consists of all the energy transformation reactions in an organism.",
                  "Metabolism manages the increase of entropy in an organism."], 3),
        Question("Which of the following statements is true concerning catabolic pathways?",
                 ["They combine molecules into more energy-rich molecules.",
                  "They supply energy, primarily in the form of ATP, for the cell's work.",
                  "They are endergonic.",
                  "They are spontaneous and do not need enzyme catalysis.",
                  "They build up complex molecules such as protein from simpler compounds."], 1),
        Question("Which of the following statements regarding enzymes is true?",
                 ["Enzymes increase the rate of a reaction by making the reaction more exergonic.",
                  "Enzymes increase the rate of a reaction by lowering the activation energy barrier.",
                  "Enzymes increase the rate of a reaction by reducing the rate of reverse reactions.",
                  "Enzymes change the equilibrium point of the reactions they catalyze.",
                  "Enzymes make the rate of a reaction independent of substrate concentrations."], 1),
        Question("Zinc, an essential trace element for most organisms, is present in the active site of the enzyme carboxypeptidase. The zinc most likely functions as a(n)",
                 ["competitive inhibitor of the enzyme.",
                  "noncompetitive inhibitor of the enzyme.",
                  "allosteric activator of the enzyme.",
                  "cofactor necessary for enzyme activity.",
                  "coenzyme derived from a vitamin."], 3),
    ]

    hw3 = [
        Question("During cellular respiration, acetyl CoA accumulates in which location?",
                 ["cytosol", "mitochondrial outer membrane", "mitochondrial inner membrane",
                  "mitochondrial intermembrane space", "mitochondrial matrix"], 4),
        Question("In chemiosmotic phosphorylation, what is the most direct source of energy that is used to convert ADP + Pi to ATP?",
                 ["energy released as electrons flow through the electron transport system",
                  "energy released from substrate-level phosphorylation",
                  "energy released from movement of protons through ATP synthase, against the electrochemical gradient",
                  "energy released from movement of protons through ATP synthase, down the electrochemical gradient",
                  "No external source of energy is required because the reaction is exergonic."], 3),
        Question("Inside an active mitochondrion, most electrons follow which pathway?",
                 ["glycolysis -> NADH -> oxidative phosphorylation -> ATP -> oxygen",
                  "citric acid cycle -> FADH2 -> electron transport chain -> ATP",
                  "electron transport chain -> citric acid cycle -> ATP -> oxygen",
                  "pyruvate -> citric acid cycle -> ATP -> NADH -> oxygen",
                  "citric acid cycle -> NADH -> electron transport chain -> oxygen"], 4),
        Question("One function of both alcohol fermentation and lactic acid fermentation is to",
                 ["reduce NAD+ to NADH.", "reduce FAD+ to FADH2.", "oxidize NADH to NAD+.", "reduce FADH2 to FAD+."], 2),
        Question("The ATP made during glycolysis is generated by",
                 ["substrate-level phosphorylation.", "electron transport.", "photophosphorylation.", "chemiosmosis.", "oxidation of NADH to NAD+."], 0),
        Question("The oxygen consumed during cellular respiration is involved directly in which process or event?",
                 ["glycolysis", "accepting electrons at the end of the electron transport chain",
                  "the citric acid cycle", "the oxidation of pyruvate to acetyl CoA",
                  "the phosphorylation of ADP to form ATP"], 1),
        Question("The transport of pyruvate into mitochondria depends on the proton-motive force across the inner mitochondrial membrane. How does pyruvate enter the mitochondrion?",
                 ["active transport", "diffusion", "facilitated diffusion", "through a channel", "through a pore"], 0),
        Question("When electrons move closer to a more electronegative atom, what happens?",
                 ["The more electronegative atom is reduced, and energy is released.",
                  "The more electronegative atom is reduced, and energy is consumed.",
                  "The more electronegative atom is oxidized, and energy is consumed.",
                  "The more electronegative atom is oxidized, and energy is released.",
                  "The more electronegative atom is reduced, and entropy decreases."], 0),
        Question("Where are the proteins of the electron transport chain located?",
                 ["cytosol", "mitochondrial outer membrane", "mitochondrial inner membrane",
                  "mitochondrial intermembrane space", "mitochondrial matrix"], 2),
        Question("Which process in eukaryotic cells will proceed normally whether oxygen (O2) is present or absent?",
                 ["electron transport", "glycolysis", "the citric acid cycle", "oxidative phosphorylation", "chemiosmosis"], 1),
    ]

    hw4 = [
        Question("As a research scientist, you measure the amount of ATP and NADPH consumed by the Calvin cycle in 1 hour. You find 30,000 molecules of ATP consumed, but only 20,000 molecules of NADPH. Where did the extra ATP molecules come from?",
                 ["photosystem II", "photosystem I", "cyclic electron flow", "linear electron flow", "chlorophyll"], 2),
        Question("CAM plants keep stomata closed in daytime, thus reducing loss of water. They can do this because they",
                 ["fix CO2 into organic acids during the night.",
                  "fix CO2 into sugars in the bundle-sheath cells.",
                  "fix CO2 into pyruvate in the mesophyll cells.",
                  "use the enzyme phosphofructokinase, which outcompetes rubisco for CO2.",
                  "use photosystems I and II at night."], 0),
        Question("In any ecosystem, terrestrial or aquatic, what group(s) is (are) always necessary?",
                 ["autotrophs and heterotrophs", "producers and primary consumers", "photosynthesizers", "autotrophs", "green plants"], 3),
        Question("In the thylakoid membranes, what is the main role of the antenna pigment molecules?",
                 ["split water and release oxygen to the reaction-center chlorophyll",
                  "harvest photons and transfer light energy to the reaction-center chlorophyll",
                  "synthesize ATP from ADP and Pi",
                  "transfer electrons to ferredoxin and then NADPH",
                  "concentrate photons within the stroma"], 1),
        Question("Photorespiration lowers the efficiency of photosynthesis by preventing the formation of",
                 ["carbon dioxide molecules.", "3-phosphoglycerate molecules", "ATP molecules.", "ribulose bisphosphate molecules.", "RuBP carboxylase molecules."], 1),
        Question("Some photosynthetic organisms contain chloroplasts that lack photosystem II, yet are able to survive. The best way to detect the lack of photosystem II in these organisms would be",
                 ["to determine if they have thylakoids in the chloroplasts.",
                  "to test for liberation of O2 in the light.",
                  "to test for CO2 fixation in the dark.",
                  "to do experiments to generate an action spectrum.",
                  "to test for production of either sucrose or starch."], 1),
        Question("When oxygen is released as a result of photosynthesis, it is a by-product of which of the following?",
                 ["reducing NADP+", "splitting the water molecules", "chemiosmosis",
                  "the electron transfer system of photosystem I", "the electron transfer system of photosystem II"], 1),
        Question("Where does the Calvin cycle take place?",
                 ["stroma of the chloroplast", "thylakoid membrane", "cytoplasm surrounding the chloroplast", "chlorophyll molecule", "outer membrane of the chloroplast"], 0),
        Question("Which of the following are products of the light reactions of photosynthesis that are utilized in the Calvin cycle?",
                 ["CO2 and glucose", "H2O and O2", "ADP, Pi, and NADP+", "electrons and H+", "ATP and NADPH"], 4),
        Question("Why are C4 plants able to photosynthesize with no apparent photorespiration?",
                 ["They do not participate in the Calvin cycle.",
                  "They use PEP carboxylase to initially fix CO2.",
                  "They are adapted to cold, wet climates.",
                  "They conserve water more efficiently.",
                  "They exclude oxygen from their tissues."], 1),
    ]

    hw5 = [
        Question("A small molecule that specifically binds to another molecule, usually a larger one",
                 ["is called a signal transducer.",
                  "is called a ligand.",
                  "is called a polymer.",
                  "seldom is involved in hormonal signaling.",
                  "usually terminates a signal reception."], 1),
        Question("Adenylyl cyclase has the opposite effect of which of the following?",
                 ["protein kinase", "protein phosphatase", "phosphodiesterase", "phosphorylase", "GTPase"], 2),
        Question("Caffeine is an inhibitor of phosphodiesterase. Therefore, the cells of a person who has recently consumed coffee would have increased levels of",
                 ["phosphorylated proteins.", "GTP.", "cAMP.", "adenylyl cyclase.", "activated G proteins."], 2),
        Question("From the perspective of the cell receiving the message, the three stages of cell signaling are",
                 ["the paracrine, local, and synaptic stages.",
                  "signal reception, signal transduction, and cellular response.",
                  "signal reception, nucleus disintegration, and new cell generation.",
                  "the alpha, beta, and gamma stages.",
                  "signal reception, cellular response, and cell division."], 1),
        Question("In general, a signal transmitted via phosphorylation of a series of proteins",
                 ["brings a conformational change to each protein.",
                  "requires binding of a hormone to a cytosol receptor.",
                  "cannot occur in yeasts because they lack protein phosphatases.",
                  "requires phosphorylase activity.",
                  "allows target cells to change their shape and therefore their activity."], 0),
        Question("Testosterone (a steroid hormone) functions inside a cell by",
                 ["acting as a signal receptor that activates ion-channel proteins.",
                  "binding with a receptor protein that enters the nucleus and activates specific genes.",
                  "acting as a steroid signal receptor that activates ion-channel proteins.",
                  "becoming a second messenger that inhibits adenylyl cyclase.",
                  "coordinating a phosphorylation cascade that increases glycogen metabolism."], 1),
        Question("The general name for an enzyme that transfers phosphate groups from ATP to a protein is",
                 ["phosphorylase.", "phosphatase.", "protein kinase.", "ATPase.", "protease."], 2),
        Question("What could happen to the target cells in an animal that lack receptors for local regulators?",
                 ["They could compensate by receiving nutrients via an a factor.",
                  "They could develop normally in response to neurotransmitters instead.",
                  "They could divide but never reach full size.",
                  "They would not be able to multiply in response to growth factors from nearby cells.",
                  "Hormones would not be able to interact with target cells."], 3),
        Question("What would be true for the signaling system in an animal cell that lacks the ability to produce GTP?",
                 ["It would not be able to activate and inactivate the G protein on the cytoplasmic side of the plasma membrane.",
                  "It could activate only the epinephrine system.",
                  "It would be able to carry out reception and transduction, but would not be able to respond to a signal.",
                  "Only A and C are true.",
                  "A, B, and C are true."], 3),
        Question("Which of the following is a CORRECT association?",
                 ["kinase activity and the addition of a tyrosine",
                  "phosphodiesterase activity and the removal of phosphate groups",
                  "Phospholipase C activity and release of calcium ions from endoplasmic reticulum",
                  "adenylyl cyclase activity and the conversion of cAMP to AMP"], 2),
    ]

    return {
        "Homework 1 (Virus basics)": hw1,
        "Homework 2 (Enzymes/Metabolism)": hw2,
        "Homework 3 (Respiration)": hw3,
        "Homework 4 (Photosynthesis/Ecology)": hw4,
        "Homework 5 (Signaling)": hw5,
    }

def load_practice_exam_pool() -> List[Question]:
    # Built from Lec2 Practice Exam PDF (50 questions). :contentReference[oaicite:1]{index=1}
    return [
        # 1–10 Viruses
        Question("The genetic material of the HIV virus consists of _____.",
                 ["single-stranded RNA", "double-stranded RNA", "none of the above", "double-stranded DNA", "single-stranded DNA"], 0),
        Question("What is the name given to viruses that are single-stranded RNA that acts as a template for DNA synthesis?",
                 ["proviruses", "retroviruses", "bacteriophages", "lytic phages", "viroids"], 1),
        Question("In the lysogenic cycle _____.",
                 ["a bacterium replicates without passing viral DNA to its daughter cells",
                  "host DNA is destroyed and viral DNA is replicated",
                  "a bacterium divides once before the lytic cycle is initiated",
                  "viral DNA is replicated along with host DNA",
                  "viral DNA is destroyed and host DNA is replicated"], 3),
        Question("Emerging viruses arise by",
                 ["the spread of existing viruses to new host species.",
                  "mutation of existing viruses.",
                  "the spread of existing viruses more widely within their host species.",
                  "mutation of existing viruses, the spread of existing viruses to new host species, and the spread of existing viruses more widely within their host species."], 3),
        Question("Viral DNA makes mRNA by the process of _____.",
                 ["lysis", "infection", "translation", "replication", "Transcription"], 4),
        Question("As a result of the lytic cycle, _____.",
                 ["a prophage is created", "viral DNA is incorporated into host cell DNA", "the host cell is not destroyed",
                  "the host cell's DNA is destroyed", "viral ribosomes are produced"], 3),
        Question("What is the source of a viral envelope?",
                 ["prophages", "provirus", "viral glycoproteins", "host cell membrane", "host cell DNA"], 3),
        Question("Antiviral drugs that have become useful are usually associated with which of the following properties?",
                 ["removal of viral proteins", "ability to remove all viruses from the infected host", "interference with viral replication",
                  "prevention of the host from becoming infected", "removal of viral mRNAs"], 2),
        Question("Clear patches in cell cultures that indicate sites of virus infection are called",
                 ["pocks", "colonies", "prions", "Plaques"], 3),
        Question("What is the function of reverse transcriptase?",
                 ["It catalyzes the formation of DNA from an RNA template.",
                  "It catalyzes the formation of a polypeptide from an RNA template.",
                  "It catalyzes the formation of RNA from a DNA template.",
                  "It catalyzes the formation of DNA from a polypeptide template.",
                  "It catalyzes the formation of RNA from a polypeptide template."], 0),

        # 11–20 Enzymes/Metabolism
        Question("Which of the following statements is true concerning catabolic pathways?",
                 ["They combine molecules into more energy-rich molecules.",
                  "They are spontaneous and do not need enzyme catalysis.",
                  "They build up complex molecules such as protein from simpler compounds.",
                  "They supply energy, primarily in the form of ATP, for the cell's work.",
                  "They are endergonic."], 3),
        Question("Which of the following is true for all exergonic reactions?",
                 ["The reaction goes only in a forward direction: all reactants will be converted to products, but no products will be converted to reactants.",
                  "The reaction proceeds with a net release of free energy.",
                  "A net input of energy from the surroundings is required for the reactions to proceed.",
                  "The products have more total energy than the reactants.",
                  "The reactions are rapid."], 1),
        Question("According to the induced fit hypothesis of enzyme catalysis, which of the following is correct?",
                 ["The binding of the substrate depends on the shape of the active site.",
                  "The binding of the substrate changes the shape of the enzyme's active site.",
                  "The active site creates a microenvironment ideal for the reaction.",
                  "A competitive inhibitor can outcompete the substrate for the active site.",
                  "Some enzymes change their structure when activators bind to the enzyme."], 1),
        Question("Which of the following statements regarding enzymes is true?",
                 ["Enzymes make the rate of a reaction independent of substrate concentrations.",
                  "Enzymes increase the rate of a reaction by making the reaction more exergonic.",
                  "Enzymes increase the rate of a reaction by reducing the rate of reverse reactions.",
                  "Enzymes change the equilibrium point of the reactions they catalyze.",
                  "Enzymes increase the rate of a reaction by lowering the activation energy barrier."], 4),
        Question("Which of the following best describes enthalpy (H)?",
                 ["the total kinetic energy of a system",
                  "the system's entropy",
                  "the heat content of a chemical system",
                  "the cell's energy equilibrium",
                  "the condition of a cell that is not able to react"], 2),
        Question("Which of the following is an example of cooperativity?",
                 ["the binding of an end product of a metabolic pathway to the first enzyme that acts in the pathway",
                  "a molecule binding at one unit of a tetramer, allowing faster binding at each of the other three",
                  "binding of an ATP molecule along with one of the substrate molecules in an active site",
                  "the effect of increasing temperature on the rate of an enzymatic reaction",
                  "one enzyme in a metabolic pathway passing its product to act as a substrate for the next enzyme in the pathway"], 1),
        Question("Which of the following is true of metabolism in its entirety in all organisms?",
                 ["Metabolism uses all of an organism's resources.",
                  "Metabolism depends on a constant supply of energy from food.",
                  "Metabolism manages the increase of entropy in an organism.",
                  "Metabolism depends on an organism's adequate hydration.",
                  "Metabolism consists of all the energy transformation reactions in an organism."], 4),
        Question("Zinc, an essential trace element for most organisms, is present in the active site of the enzyme carboxypeptidase. The zinc most likely functions as a(n)",
                 ["noncompetitive inhibitor of the enzyme.",
                  "coenzyme derived from a vitamin.",
                  "allosteric activator of the enzyme.",
                  "cofactor necessary for enzyme activity.",
                  "competitive inhibitor of the enzyme."], 3),
        Question("The mathematical expression for the change in free energy of a system is ?G = ?H - T?S. Which of the following is (are) correct?",
                 ["?S is the change in enthalpy, a measure of randomness.",
                  "?G is the change in free energy.",
                  "?H is the change in entropy, the energy available to do work.",
                  "T is the temperature in degrees Celsius."], 1),
        Question("Besides turning enzymes on or off, what other means does a cell use to control enzymatic activity?",
                 ["hydrophobic interactions",
                  "cessation of cellular protein synthesis",
                  "connecting enzymes into large aggregates",
                  "exporting enzymes out of the cell",
                  "localization of enzymes into specific organelles or membranes"], 4),

        # 21–30 Respiration
        Question("One function of both alcohol fermentation and lactic acid fermentation is to",
                 ["oxidize NADH to NAD+.",
                  "reduce FADH2 to FAD+.",
                  "reduce NAD+ to NADH.",
                  "reduce FAD+ to FADH2."], 0),
        Question("In chemiosmotic phosphorylation, what is the most direct source of energy that is used to convert ADP + Pi to ATP?",
                 ["energy released from substrate-level phosphorylation",
                  "No external source of energy is required because the reaction is exergonic.",
                  "energy released from movement of protons through ATP synthase, against the electrochemical gradient",
                  "energy released as electrons flow through the electron transport system",
                  "energy released from movement of protons through ATP synthase, down the electrochemical gradient"], 4),
        Question("Inside an active mitochondrion, most electrons follow which pathway?",
                 ["citric acid cycle -> NADH -> electron transport chain -> oxygen",
                  "electron transport chain -> citric acid cycle -> ATP -> oxygen",
                  "glycolysis -> NADH -> oxidative phosphorylation -> ATP -> oxygen",
                  "citric acid cycle -> FADH2 -> electron transport chain -> ATP",
                  "pyruvate -> citric acid cycle -> ATP -> NADH -> oxygen"], 0),
        Question("During cellular respiration, acetyl CoA accumulates in which location?",
                 ["mitochondrial matrix", "mitochondrial intermembrane space", "cytosol", "mitochondrial outer membrane", "mitochondrial inner membrane"], 0),
        Question("When electrons move closer to a more electronegative atom, what happens?",
                 ["The more electronegative atom is reduced, and entropy decreases.",
                  "The more electronegative atom is oxidized, and energy is released.",
                  "The more electronegative atom is oxidized, and energy is consumed.",
                  "The more electronegative atom is reduced, and energy is consumed.",
                  "The more electronegative atom is reduced, and energy is released."], 4),
        Question("Which process in eukaryotic cells will proceed normally whether oxygen (O2) is present or absent?",
                 ["chemiosmosis", "electron transport", "oxidative phosphorylation", "glycolysis", "the citric acid cycle"], 3),
        Question("The ATP made during glycolysis is generated by",
                 ["photophosphorylation.", "electron transport.", "chemiosmosis.", "substrate-level phosphorylation.", "oxidation of NADH to NAD+."], 3),
        Question("The transport of pyruvate into mitochondria depends on the proton-motive force across the inner mitochondrial membrane. How does pyruvate enter the mitochondrion?",
                 ["facilitated diffusion", "through a channel", "active transport", "through a pore", "diffusion"], 2),
        Question("The oxygen consumed during cellular respiration is involved directly in which process or event?",
                 ["the phosphorylation of ADP to form ATP",
                  "the oxidation of pyruvate to acetyl CoA",
                  "accepting electrons at the end of the electron transport chain",
                  "glycolysis",
                  "the citric acid cycle"], 2),
        Question("Where are the proteins of the electron transport chain located?",
                 ["mitochondrial outer membrane", "mitochondrial matrix", "mitochondrial intermembrane space", "cytosol", "mitochondrial inner membrane"], 4),

        # 31–40 Photosynthesis/Ecology
        Question("In any ecosystem, terrestrial or aquatic, what group(s) is (are) always necessary?",
                 ["green plants", "autotrophs and heterotrophs", "autotrophs", "producers and primary consumers", "photosynthesizers"], 2),
        Question("As a research scientist, you measure the amount of ATP and NADPH consumed by the Calvin cycle in 1 hour. You find 30,000 molecules of ATP consumed, but only 20,000 molecules of NADPH. Where did the extra ATP molecules come from?",
                 ["cyclic electron flow", "photosystem I", "chlorophyll", "linear electron flow", "photosystem II"], 0),
        Question("Which of the following are products of the light reactions of photosynthesis that are utilized in the Calvin cycle?",
                 ["electrons and H+", "ATP and NADPH", "ADP, Pi, and NADP+", "CO2 and glucose", "H2O and O2"], 1),
        Question("Photorespiration lowers the efficiency of photosynthesis by preventing the formation of",
                 ["ATP molecules.", "ribulose bisphosphate molecules.", "RuBP carboxylase molecules.", "3-phosphoglycerate molecules", "carbon dioxide molecules."], 3),
        Question("CAM plants keep stomata closed in daytime, thus reducing loss of water. They can do this because they",
                 ["use photosystems I and II at night.",
                  "fix CO2 into pyruvate in the mesophyll cells.",
                  "use the enzyme phosphofructokinase, which outcompetes rubisco for CO2.",
                  "fix CO2 into sugars in the bundle-sheath cells.",
                  "fix CO2 into organic acids during the night."], 4),
        Question("Why are C4 plants able to photosynthesize with no apparent photorespiration?",
                 ["They are adapted to cold, wet climates.",
                  "They conserve water more efficiently.",
                  "They exclude oxygen from their tissues.",
                  "They use PEP carboxylase to initially fix CO2.",
                  "They do not participate in the Calvin cycle."], 3),
        Question("When oxygen is released as a result of photosynthesis, it is a by-product of which of the following?",
                 ["the electron transfer system of photosystem II",
                  "reducing NADP+",
                  "chemiosmosis",
                  "the electron transfer system of photosystem I",
                  "splitting the water molecules"], 4),
        Question("Where does the Calvin cycle take place?",
                 ["outer membrane of the chloroplast", "stroma of the chloroplast", "thylakoid membrane", "cytoplasm surrounding the chloroplast", "chlorophyll molecule"], 1),
        Question("In the thylakoid membranes, what is the main role of the antenna pigment molecules?",
                 ["transfer electrons to ferredoxin and then NADPH",
                  "synthesize ATP from ADP and Pi",
                  "split water and release oxygen to the reaction-center chlorophyll",
                  "harvest photons and transfer light energy to the reaction-center chlorophyll",
                  "concentrate photons within the stroma"], 3),
        Question("Some photosynthetic organisms contain chloroplasts that lack photosystem II, yet are able to survive. The best way to detect the lack of photosystem II in these organisms would be",
                 ["to test for liberation of O2 in the light.",
                  "to do experiments to generate an action spectrum.",
                  "to determine if they have thylakoids in the chloroplasts.",
                  "to test for CO2 fixation in the dark.",
                  "to test for production of either sucrose or starch."], 0),

        # 41–50 Signaling
        Question("Adenylyl cyclase has the opposite effect of which of the following?",
                 ["GTPase", "protein kinase", "protein phosphatase", "phosphorylase", "phosphodiesterase"], 4),
        Question("Testosterone (a steroid hormone) functions inside a cell by",
                 ["becoming a second messenger that inhibits adenylyl cyclase.",
                  "coordinating a phosphorylation cascade that increases glycogen metabolism.",
                  "binding with a receptor protein that enters the nucleus and activates specific genes.",
                  "acting as a signal receptor that activates ion-channel proteins.",
                  "acting as a steroid signal receptor that activates ion-channel proteins."], 2),
        Question("What would be true for the signaling system in an animal cell that lacks the ability to produce GTP?",
                 ["It could activate only the epinephrine system.",
                  "Only A and C are true.",
                  "It would be able to carry out reception and transduction, but would not be able to respond to a signal.",
                  "A, B, and C are true.",
                  "It would not be able to activate and inactivate the G protein on the cytoplasmic side of the plasma membrane."], 1),
        Question("A small molecule that specifically binds to another molecule, usually a larger one",
                 ["is called a signal transducer.",
                  "usually terminates a signal reception.",
                  "seldom is involved in hormonal signaling.",
                  "is called a polymer.",
                  "is called a ligand."], 4),
        Question("In general, a signal transmitted via phosphorylation of a series of proteins",
                 ["requires phosphorylase activity.",
                  "requires binding of a hormone to a cytosol receptor.",
                  "brings a conformational change to each protein.",
                  "allows target cells to change their shape and therefore their activity.",
                  "cannot occur in yeasts because they lack protein phosphatases."], 2),
        Question("Which of the following is a CORRECT association?",
                 ["adenylyl cyclase activity and the conversion of cAMP to AMP",
                  "kinase activity and the addition of a tyrosine",
                  "Phospholipase C activity and release of calcium ions from endoplasmic reticulum",
                  "phosphodiesterase activity and the removal of phosphate groups"], 2),
        Question("From the perspective of the cell receiving the message, the three stages of cell signaling are",
                 ["signal reception, cellular response, and cell division.",
                  "signal reception, signal transduction, and cellular response.",
                  "signal reception, nucleus disintegration, and new cell generation.",
                  "the alpha, beta, and gamma stages.",
                  "the paracrine, local, and synaptic stages."], 1),
        Question("Caffeine is an inhibitor of phosphodiesterase. Therefore, the cells of a person who has recently consumed coffee would have increased levels of",
                 ["GTP.", "cAMP.", "adenylyl cyclase.", "phosphorylated proteins.", "activated G proteins."], 1),
        Question("The general name for an enzyme that transfers phosphate groups from ATP to a protein is",
                 ["protein kinase.", "ATPase.", "phosphorylase.", "phosphatase.", "protease."], 0),
        Question("What could happen to the target cells in an animal that lack receptors for local regulators?",
                 ["They could divide but never reach full size.",
                  "Hormones would not be able to interact with target cells.",
                  "They could compensate by receiving nutrients via an a factor.",
                  "They would not be able to multiply in response to growth factors from nearby cells.",
                  "They could develop normally in response to neurotransmitters instead."], 3),
    ]

def split_practice_exam_into_chapters(practice_exam: List[Question]) -> Dict[str, List[Question]]:
    if len(practice_exam) != 50:
        raise ValueError(f"Expected 50 practice exam questions, got {len(practice_exam)}")
    return {
        "Chapter: Viruses": practice_exam[0:10],
        "Chapter: Enzymes & Metabolism": practice_exam[10:20],
        "Chapter: Cellular Respiration": practice_exam[20:30],
        "Chapter: Photosynthesis & Ecology": practice_exam[30:40],
        "Chapter: Cell Signaling": practice_exam[40:50],
    }

def chapter_pool_names():
    return [
        "Chapter: Viruses",
        "Chapter: Enzymes & Metabolism",
        "Chapter: Cellular Respiration",
        "Chapter: Photosynthesis & Ecology",
        "Chapter: Cell Signaling",
    ]

# ---------------- App state helpers ----------------
def init_state():
    defaults = {
        "step": "mode",              # mode -> pools -> quiz -> done
        "mode": None,                # exam/practice
        "choose_style": "assignment",# assignment/chapter
        "selected_questions": [],
        "order": [],
        "idx": 0,
        "score": 0,
        "needs_retry": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def start_quiz(qs: List[Question]):
    st.session_state.selected_questions = qs
    st.session_state.order = list(range(len(qs)))
    random.shuffle(st.session_state.order)
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.needs_retry = False
    st.session_state.step = "quiz"

# ---------------- Main ----------------
def main():
    st.set_page_config(page_title="MCB Exam #2 Quiz", page_icon="🧠", layout="centered")
    init_state()

    hw_pools = load_homework_pools()
    pe_all = load_practice_exam_pool()
    pe_by_chapter = split_practice_exam_into_chapters(pe_all) if pe_all else {c: [] for c in chapter_pool_names()}

    st.title("🧠 MCB Lecture Exam #2 Quiz")

    # ---------- Step: MODE ----------
    if st.session_state.step == "mode":
        st.subheader("Choose a mode")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Exam Mode (score at end)", use_container_width=True):
                st.session_state.mode = "exam"
                st.session_state.step = "pools"
        with col2:
            if st.button("Practice Mode (instant feedback + retry)", use_container_width=True):
                st.session_state.mode = "practice"
                st.session_state.step = "pools"
        st.info("Tip: On iPhone, you can Share → Add to Home Screen for an app-like icon.")
        return

    # ---------- Step: POOLS ----------
    if st.session_state.step == "pools":
        st.subheader("Select question pools")

        st.session_state.choose_style = st.radio(
            "Choose content by:",
            ["assignment", "chapter"],
            format_func=lambda x: "Assignment" if x == "assignment" else "Chapter",
            horizontal=True
        )

        selected = []

        if st.session_state.choose_style == "assignment":
            st.write("### By assignment")
            # default checked
            picks = {}
            for name, qs in hw_pools.items():
                picks[name] = st.checkbox(f"{name} ({len(qs)} questions)", value=True)
            pe_pick = st.checkbox(f"Practice Exam (Lecture 2) ({len(pe_all)} questions)", value=True)

            for name, on in picks.items():
                if on:
                    selected.extend(hw_pools[name])
            if pe_pick:
                selected.extend(pe_all)

        else:
            st.write("### By chapter")
            # build chapter pools: HW topic + practice exam topic
            hw_by_chapter = {
                "Chapter: Viruses": hw_pools.get("Homework 1 (Virus basics)", []),
                "Chapter: Enzymes & Metabolism": hw_pools.get("Homework 2 (Enzymes/Metabolism)", []),
                "Chapter: Cellular Respiration": hw_pools.get("Homework 3 (Respiration)", []),
                "Chapter: Photosynthesis & Ecology": hw_pools.get("Homework 4 (Photosynthesis/Ecology)", []),
                "Chapter: Cell Signaling": hw_pools.get("Homework 5 (Signaling)", []),
            }
            for chap in chapter_pool_names():
                chap_qs = hw_by_chapter[chap] + pe_by_chapter.get(chap, [])
                on = st.checkbox(f"{chap} ({len(chap_qs)} questions)", value=True)
                if on:
                    selected.extend(chap_qs)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("⬅ Back", use_container_width=True):
                st.session_state.step = "mode"
                return
        with c2:
            if st.button("▶ Start", use_container_width=True):
                if not selected:
                    st.error("Select at least one pool.")
                    return
                start_quiz(selected)
                return

        st.caption(f"Selected questions: {len(selected)}")
        return

    # ---------- Step: QUIZ ----------
    if st.session_state.step == "quiz":
        qs = st.session_state.selected_questions
        total = len(qs)
        q = qs[st.session_state.order[st.session_state.idx]]

        st.progress((st.session_state.idx + 1) / total)
        st.write(f"**Question {st.session_state.idx + 1} / {total}**  •  Mode: **{st.session_state.mode.upper()}**")
        st.write("### " + q.prompt)

        # In practice mode, if you got it wrong, you must retry the same question
        choice = st.radio("Choose one:", q.options, index=None)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Quit to pool select", use_container_width=True):
                st.session_state.step = "pools"
                return

        with col2:
            if st.button("Submit", use_container_width=True):
                if choice is None:
                    st.warning("Pick an answer first.")
                    return
                chosen_idx = q.options.index(choice)
                correct = (chosen_idx == q.correct)

                if st.session_state.mode == "practice":
                    if correct:
                        st.success("✅ Correct")
                        st.session_state.score += 1
                        st.session_state.idx += 1
                    else:
                        st.error("❌ Wrong — retry this one")
                        # do not advance
                    if st.session_state.idx >= total:
                        st.session_state.step = "done"
                    st.rerun()
                else:
                    if correct:
                        st.session_state.score += 1
                    st.session_state.idx += 1
                    if st.session_state.idx >= total:
                        st.session_state.step = "done"
                    st.rerun()

    # ---------- Step: DONE ----------
    if st.session_state.step == "done":
        st.subheader("Done!")
        total = len(st.session_state.selected_questions)
        if st.session_state.mode == "exam":
            pct = (st.session_state.score / total) * 100
            st.success(f"Score: {st.session_state.score}/{total} ({pct:.1f}%)")
        else:
            st.success("Practice complete — nice work.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("New session", use_container_width=True):
                st.session_state.step = "mode"
                return
        with col2:
            if st.button("Pool select", use_container_width=True):
                st.session_state.step = "pools"
                return


if __name__ == "__main__":
    main()