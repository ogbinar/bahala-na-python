name: Chapter Proposal
title: "[chapter]: "
labels: ["chapter-proposal"]
body:
  - type: markdown
    attributes:
      value: |
        Propose a new chapter or section for the book.
  - type: input
    id: title
    attributes:
      label: Chapter title
      description: What should this chapter be about?
    validations:
      required: true
  - type: input
    id: part
    attributes:
      label: Which part?
      description: Part 1 (Fundamentals), Part 2 (Building Things), Part 3 (Going Further), or Part 4 (Capstone)?
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: Description
      description: What will this chapter teach? What Filipino context does it use?
    validations:
      required: true
  - type: textarea
    id: concepts
    attributes:
      label: Python concepts covered
      description: What Python concepts will this chapter introduce?
    validations:
      required: true
  - type: textarea
    id: project
    attributes:
      label: Project / exercise
      description: What project or exercise will readers build?
    validations:
      required: true
