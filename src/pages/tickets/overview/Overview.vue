<template>
<div class="main-content">

  <!-- HEADER -->
  <div class="pt-7 pb-8 bg-dark bg-ellipses">
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-md-10 col-lg-8 col-xl-6">

          <div class="mb-5 d-flex row justify-content-center">

            <img width="300px" src="@/assets/whitelogo.png"/>

          </div>

          <!-- Text -->
          <p class="lead text-center text-muted">
            Be part of leiriacon. Buy you ticket now to have guaranteed entry.
          </p>

        </div>
      </div> <!-- / .row -->
    </div>
  </div>

  <!-- CONTENT -->
  <div class="container-fluid">
    <div class="row mt-n7 justify-content-center">
      <div class="col-12 col-lg-4">

        <!-- Card -->
        <div class="card">
          <div class="card-body">

            <!-- Title -->
            <h6 class="text-uppercase text-center text-muted my-4">
              Associate
            </h6>

            <!-- Price -->
            <div class="row g-0 align-items-center justify-content-center">
              <div class="col-auto">
                <div class="h2 mb-0">€</div>
              </div>
              <div class="col-auto">
                <div class="display-2 mb-0">5</div>
              </div>
              <div class="d-flex align-self-start justify-content-start">
                <s class="align-self-start h1 text-muted mt-1">10</s>
              </div>
            </div> <!-- / .row -->

            <!-- Period -->
            <div class="h6 text-uppercase text-center text-muted mb-5">
              / person
            </div>

            <!-- Features -->
            <div class="mb-3">
              <ul class="list-group list-group-flush">
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <div>
                    <small>Personalized Badge</small>
                    <b-link v-b-tooltip:hover class="ml-2 text-info" title="Only for buyer"><b-icon-info-circle-fill/></b-link>
                  </div>
                  <i class="fe fe-check-circle text-success"></i>
                </li>
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <small>Full access</small> <i class="fe fe-check-circle text-success"></i>
                </li>
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <small>4-days</small> <i class="fe fe-check-circle text-success"></i>
                </li>
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <small>Additional tickets</small> <small>3</small>
                </li>
              </ul>
            </div>

            <!-- Button -->
            <b-button v-b-modal.buy-tickets-modal variant="primary" block>
              Buy
            </b-button>

          </div>
        </div>

      </div>
      <div class="col-12 col-lg-4">

        <!-- Card -->
        <div class="card">
          <div class="card-body">

            <!-- Title -->
            <h6 class="text-uppercase text-center text-muted my-4">
              Standard
            </h6>

            <!-- Price -->
            <div class="row g-0 align-items-center justify-content-center">
              <div class="col-auto">
                <div class="h2 mb-0">€</div>
              </div>
              <div class="col-auto">
                <div class="display-2 mb-0">5</div>
              </div>
              <div class="d-flex align-self-start justify-content-start">
                <s class="align-self-start h1 text-muted mt-1">10</s>
              </div>
            </div> <!-- / .row -->

            <!-- Period -->
            <div class="h6 text-uppercase text-center text-muted mb-5">
              / person
            </div>

            <!-- Features -->
            <div class="mb-3">
              <ul class="list-group list-group-flush">
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <small>Full access</small> <i class="fe fe-check-circle text-success"></i>
                </li>
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <small>4-days</small> <i class="fe fe-check-circle text-success"></i>
                </li>
                <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                  <small>Additional tickets</small> <small>3</small>
                </li>
              </ul>
            </div>

            <!-- Button -->
            <b-button variant="light" block disabled>
              Coming December 1st
            </b-button>

          </div>
        </div>

      </div>
    </div> <!-- / .row -->
    <div class="row justify-content-center">
      <div class="col-12 col-md-6">

        <!-- Card -->
        <div class="card card-inactive">
          <div class="card-body">

            <!-- Title -->
            <h3 class="text-center">
              4-day ticket
            </h3>

            <!-- Text -->
            <p class="text-muted text-center">
              All tickets gives you access to the convention during all days.
            </p>

          </div>
        </div>

      </div>
      <div class="col-12 col-md-6">

        <!-- Card -->
        <div class="card card-inactive">
          <div class="card-body">

            <!-- Title -->
            <h3 class="text-center">
              Want to become an Associate?
            </h3>

            <!-- Text -->
            <p class="text-muted text-center">
              You can become an Associate at any time, we have great benefits for you.
            </p>

            <!-- Button -->
            <div class="text-center">

              <b-button href="https://www.spielportugal.org/membership" class="btn" variant="outline-secondary">
                See more
              </b-button>
            </div>

          </div>
        </div>

      </div>
    </div> <!-- / .row -->
    <Modal/>
  </div>
<b-modal>

</b-modal>
</div>
</template>

<script>
import Modal from "./partials/Modal.vue"

export default {
  name: "Buy",
  components: {Modal}
}
</script>

<style scoped>

</style>
